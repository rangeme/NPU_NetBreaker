#coding: gbk
import wx
import getpass
import base64
import os
import webbrowser
import time
import requests
import threading
from wx.lib.embeddedimage import PyEmbeddedImage

AppIcon2 = PyEmbeddedImage(
    "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"
    "3/X7SfA3DST6Oq9Bg1gAAAAASUVORK5CYII=")
getAppIcon2Data = AppIcon2.GetData
getAppIcon2Image = AppIcon2.GetImage
getAppIcon2Bitmap = AppIcon2.GetBitmap
TRAY_TOOLTIP = 'NetBreaker v1.0'

def alert(text):
    dlg = wx.MessageDialog(None, text, "alert", wx.OK)
    dlg.ShowModal()
    dlg.Destroy()

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "编辑你的用户名和密码", size=(470,270))
        try:
            
            f = open('c:/users/%s/.networker/config.conf' % getpass.getuser(), 'r')
            text = f.read()
            if text != '':
                username, password = text.split(':')
            else:
                username, password = "", ""
        except Exception, e:
            if not os.path.exists("c:/users/%s/.networker/" % getpass.getuser()):
                os.makedirs('c:/users/%s/.networker/' % getpass.getuser())
            f = open('c:/users/%s/.networker/config.conf' % getpass.getuser(), "w")
            f.close()
            username, password = "", ""
        finally:
            #print username, password
            self.panel = wx.Panel(self,-1)
            wx.StaticText(self.panel,-1,"账户：",(105,52))
            wx.StaticText(self.panel,-1,"密码：",(105,102))
            self.button=wx.Button(self.panel,-1,"确定",pos=(180,150),size=(100,30),style=wx.BU_EXACTFIT)
            self.button.Bind(wx.EVT_BUTTON,self.OnClick)
            self.text = wx.TextCtrl(self.panel, -1, username, size=(175, -1), pos=(145, 50))
            self.text.SetInsertionPoint(0)  
            self.pwd = wx.TextCtrl(self.panel, -1, base64.b64decode(password), size=(175, -1), style=wx.TE_PASSWORD, pos=(145, 100))
            self.pwd.SetInsertionPoint(0)  

    def OnClick(self, event):
        try:
            username = self.text.GetValue()
            password = self.pwd.GetValue()
            with open('c:/users/%s/.networker/config.conf' % getpass.getuser(), 'w') as f:
                f.write(username)
                f.write(':')
                f.write(base64.b64encode(password))
            dlg = wx.MessageDialog(None, "修改成功", "OK", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.Close(True)
        except Exception, e:
            dlg = wx.MessageDialog(None, "修改失败", "False", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.Close(True)

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.SetIcon(AppIcon2.GetIcon())
        self.menu2_status = True
        self.menu3_status = False
        self.time = 300
        self.sub1 = 0
        self.sub2 = 2
        self.sub3 = 0
        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.AppendItem(wx.MenuItem(menu, -1, "胸大NetBreaker v1.0"))
        menu.AppendSeparator()
        self.menu1 = self.create_menu_item(menu, '编辑', self.edit)
        self.menu2 = self.create_menu_item(menu, '连接', self.network)
        self.menu3 = self.create_menu_item(menu, '断开', self.disconnect)
        self.menu4 = self.create_menu_item(menu, '帮助', self.help)
        menu.AppendSeparator()
        self.menu6 = self.create_menu_item(menu, '退出', self.on_exit)
        self.menu2.Enable(self.menu2_status)
        self.menu3.Enable(self.menu3_status)
        return menu

    def create_menu_item(self, menu, label, func):
        item = wx.MenuItem(menu, -1, label)
        menu.Bind(wx.EVT_MENU, func, id=item.GetId())
        menu.AppendItem(item)
        return item
        
        
    def edit(self, event):
        frame=TestFrame()
        frame.Show()
        
    def conn(self, username, password):
        post_url = "http://202.117.80.138:8080/portal/pws?t=li"
        data = "userName=" + username + "&userPwd=" + password + "&serviceTypeHIDE=&serviceType=&isSavePwd=on&userurl=&userip=&basip=&language=Chinese&usermac=null&entrance=null&custompath=templatePage%2F20140225230636305&portalProxyIP=202.117.80.138&portalProxyPort=50200&dcPwdNeedEncrypt=1&assignIpType=0&appRootUrl=http%3A%2F%2F202.117.80.138%3A8080%2Fportal%2F&manualUrl=&manualUrlEncryptKey="
        self.menu2_status = False
        self.menu3_status = True
        self.connect = True
        try:
            while(self.connect):
                res = requests.post(url = post_url, data = data, headers = {'Accept-Language': 'zh-CN,zh;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',"Accept": "text/plain, */*; q=0.01", "Content-Length": len(data),'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}, timeout=20)
                content = base64.b64decode(res.content + '=======')
                if content.find('portServIncludeFailedReason') != -1:
                    self.menu2_status = True
                    self.menu3_status = False
                    alert("账户认证失败，请更换账户")
                    self.connect = False
                else:
                    time.sleep(self.time)
        except Exception, e:
            self.menu2_status = True
            self.menu3_status = False
            alert("网络错误，请检查网络")
    
    def network(self, event):
        try:
            f = open('c:/users/%s/.networker/config.conf' % getpass.getuser(), 'r')
            text = f.read()
            if text != '':
                username, password = text.split(':')
            else:
                username, password = "", ""
            thread = threading.Thread(target=self.conn, args=(username, password))
            thread.setDaemon(True)
            thread.start()
        except Exception, e:
            alert("请编辑用户名密码后使用！")
            
    def disconn(self):
        try:
            get_url = "http://202.117.80.138:8080/portal/pws?t=lo&language=Chinese&userip=&basip="
            requests.get(get_url, headers = {'Accept-Language': 'zh-CN,zh;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',"Accept": "text/plain, */*; q=0.01"})
        except Exception, e:
            alert('网络错误，下线失败')
            
    def disconnect(self, event):
        self.connect = False
        thread = threading.Thread(target=self.conn, args=(username, password))
        thread.setDaemon(True)
        thread.start()
        self.menu2_status = True
        self.menu3_status = False
        
    def help(self, event):
        dlg = wx.MessageDialog(None, "填写账户密码后点击连接(默认5分钟刷新一次)，点击转向github----by range", "Help", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            webbrowser.open("https://github.com/rangeme/NPU_NetBreaker/")  
        dlg.Destroy()

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

if __name__ == '__main__':
    app = wx.App()
    TaskBarIcon()
    app.MainLoop()
