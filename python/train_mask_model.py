import numpy as np
import os.path as path
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflowjs as tfjs
import tensorflow.keras.optimizers as optimizers
import tensorflow.keras.layers as layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow import keras
from sklearn.metrics import classification_report

# dosya yolları ve genel ayarlar
CWD = path.dirname(path.realpath(__file__))

TRAIN_DIR = path.join(CWD,'dataset','train')
VALID_DIR = path.join(CWD,'dataset','validation')
TEST_DIR = path.join(CWD,'dataset','test_large')

AI_MASK_MODEL_DIR = path.join(CWD,'ai_mask_model')
AI_MASK_MODEL_PATH = path.join(CWD,'ai_mask_model','mask_model.h5')

LOG_DIR = path.join(CWD,'train_logs')
LOG_FILE = path.join(LOG_DIR,'test_report.txt')
LOG_IMAGE = path.join(LOG_DIR,'ai_mask_model_xy.png')

# ayarlar 
NUM_CLASSES = 3
IMG_SIZE = 128
SHAPE = (IMG_SIZE, IMG_SIZE, 3)
TRAIN_BATCH_SIZE = 50
VALID_BATCH_SIZE = 50
TEST_BATCH_SIZE = 10
EPOCHS = 6
INIT_LR = 0.0006
OPTIMIZER= optimizers.Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)

# all images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, shear_range=0.15,width_shift_range=0.15,height_shift_range=0.15, zoom_range=0.15, horizontal_flip=True)

# this is the augmentation configuration we will use for testing, only rescaling
valid_datagen = ImageDataGenerator(rescale=1./255)

# test amaclı
test_datagen = ImageDataGenerator(rescale=1./255)


# Flow training images in batches of 128 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=TRAIN_BATCH_SIZE,
    class_mode='categorical')

valid_generator = valid_datagen.flow_from_directory(
    VALID_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=VALID_BATCH_SIZE,
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=TEST_BATCH_SIZE,
    shuffle=False,
    class_mode='categorical')

class_names = train_generator.class_indices
print(class_names)

"""
# confirm the iterator works
batchX, batchy = train_generator.next()
print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))

plt.figure(figsize=(10, 10))
for i in range(16):
    image = batchX[i]
    image = image * 255

    label = batchy[i]
    cname = 'doğru'
    if label[1] > 0: cname = 'hatalı'
    if label[2] > 0: cname = 'normal'

    ax = plt.subplot(4, 4, i + 1)
    plt.imshow(image.astype("uint8"))
    plt.title(cname)
    plt.axis("off")
plt.show()
"""

# Medikal Yüz Maskesi Algılama Modeli, "Transfer Öğrenme" yöntemi kullanılmıştır.
# CNN, Evrişimli Sinir Ağı katmanı girdi olarak görsel alır. 
# Görüntü boyu ve genişliği 128px. SHAPE = (128,128,3)
MaskeModel = keras.Sequential(name="happy_index")
inputLayer = layers.Input(shape=SHAPE)
baseLayer = MobileNetV2(weights="imagenet", include_top=False, input_shape=SHAPE,input_tensor=inputLayer)
for layer in baseLayer.layers: layer.trainable = False
MaskeModel.add(baseLayer)

# Pooling (havuzlama) katmanı boyutsallığı azaltma amacındadır.
# Gereksiz özellikler yok sayılarak daha önemli özelliklere odaklanılır.
# Bu sayede hem gereken işlem gücü azalır.
MaskeModel.add(layers.MaxPooling2D(pool_size=(4, 4), name="pooling_layer"))
MaskeModel.add(layers.BatchNormalization(axis=-1,momentum=0.8))

# Klasik Sinir Ağı için verileri hazırlar.
MaskeModel.add(layers.Flatten( name="flatten_layer"))
MaskeModel.add(layers.Dropout(0.4))

# 160 birimden oluşan klasik katman, relu aktivasyon fonksiyonu kullanıldı.
MaskeModel.add(layers.Dense(160,use_bias=False, name="dense_layer"))
MaskeModel.add(layers.BatchNormalization(axis=-1,momentum=0.8))
MaskeModel.add(layers.ReLU())

# Eğitim işlemi sırasında katmandan rasgele bir dizi veri üretir.
# Aşırı öğrenmeyi(overfitting) engellemek için kullanır.
# 0-1 arasında değer alır, %50(0.5) oranında rasgele veri üret anlamına gelir. 
MaskeModel.add(layers.Dropout(0.4, name="dropout_layer"))

# Çıktı katmanı 3 adet çıktımız olacak, maske_dogru, maske_yanlis, maske_yok.
MaskeModel.add(layers.Dense(NUM_CLASSES, activation="softmax", name="output_layer"))
MaskeModel.compile(optimizer=OPTIMIZER, loss="categorical_crossentropy", metrics=['categorical_accuracy'])
if path.exists(AI_MASK_MODEL_PATH): MaskeModel.load_weights(AI_MASK_MODEL_PATH)

# modeli eğit
Header = MaskeModel.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // TRAIN_BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=valid_generator,
    batch_size=TRAIN_BATCH_SIZE,
    verbose=1,
    validation_steps=valid_generator.samples // VALID_BATCH_SIZE)

tfjs.converters.save_keras_model(MaskeModel, AI_MASK_MODEL_DIR, weight_shard_size_bytes=1024*1024*4*3)
MaskeModel.save(AI_MASK_MODEL_PATH,save_format='h5',include_optimizer=False)

# test sonuc raporunu yazdır
print("test sonuc raporunu yazdır\n")
score = MaskeModel.evaluate(test_generator)
print('Test loss:', score[0]*100)
print('Test accuracy:', score[1]*100)

# predict the class label
predict=MaskeModel.predict(test_generator)
pred_classes = predict.argmax(axis=-1)
true_classes = test_generator.classes

raport = classification_report(true_classes, pred_classes, target_names=['maske dogru','maske yanlış','maske yok'])
print("\n%s\n" % (raport))

# eğitim sonucunu göster
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, EPOCHS), Header.history["loss"], label="eğitim kaybı (loss)")
plt.plot(np.arange(0, EPOCHS), Header.history["val_loss"], label="test kaybı (val_loss)")
plt.plot(np.arange(0, EPOCHS), Header.history["categorical_accuracy"], label="eğitim doğruluğu (acc)")
plt.plot(np.arange(0, EPOCHS), Header.history["val_categorical_accuracy"], label="test doğruluğu (val_acc)")
#plt.xlabel("Happy Index, Mask Model")
#plt.ylabel("Kayıp/Doğruluk")
plt.legend(loc="lower left")
plt.show()

## https://www.dlology.com/blog/one-simple-trick-to-train-keras-model-faster-with-batch-normalization/
## https://stackoverflow.com/questions/53037510/can-flow-from-directory-get-train-and-validation-data-from-the-same-directory-in
## https://www.tensorflow.org/addons/tutorials/average_optimizers_callback?hl=en