const { app ,BrowserWindow , Menu,} = require('electron');

const windowSettings =
{
    width: 1260,
    height: 700,
    show: false,
    resizable: true,
    icon: __dirname +"/assets/icon.png",
    center: true,
    //fullscreen:true,
    webPreferences: { 
        nodeIntegration: true
        //sandbox: true
    }
};

const menuItems =
[
    {
        label: 'Hakında',
    },
    {
        label: 'Geliştirme Araçları',
        submenu:
        [
            {
                label: 'Geliştirme Araçları',
                accelerator: 'CmdOrCtrl+I',
                click(item, focusedWindow)
                {
                    focusedWindow.toggleDevTools();
                }
            },
            {
                label: 'Yenile',
                role: 'reload'
            },
            {
                label: 'Kapat',
                accelerator: 'CmdOrCtrl+Q',
                click()
                {
                    app.quit();
                }
            },
        ]
    }
];

const IS_MAC = process.platform == 'darwin';

// Ana pencere
var MainWindow = null;

function createMainWindow()
{
    //maskeai.start();
    MainWindow = new BrowserWindow(windowSettings);
    MainWindow.loadFile('index.html');

    MainWindow.once('ready-to-show', () =>{
        var mainMenu = Menu.buildFromTemplate(menuItems);
        Menu.setApplicationMenu(mainMenu);
        MainWindow.maximize();
        MainWindow.show();
    });

    MainWindow.on('closed', () => { MainWindow = null; });
}


//if(!app.requestSingleInstanceLock()) app.quit();

//app.enableSandbox();
app.on('ready', ()=>{
    createMainWindow();
});

app.on('window-all-closed', () =>
{ 
    if(!IS_MAC) app.quit();
});

app.on('activate', () =>
{
    if(BrowserWindow.getAllWindows().length == 0)
    {
       MainWindow = createMainWindow();
    }
});

