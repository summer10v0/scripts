; 取消重复运行警告
#SingleInstance force

#Include utils.ahk

; 放行快捷键（普通键当修饰键用，会导致相关快捷键失效） 
$Space::Send {Space}
+Space::Send +{Space}
!Space::Send !{Space}

; 【数字键盘映射】空格+qwe asd zxc，映射成小数字键盘
Space & z::Send 1   
Space & x::Send 2
Space & c::Send 3
Space & a::Send 4
Space & s::Send 5
Space & d::Send 6
Space & q::Send 7
Space & w::Send 8
Space & e::Send 9

; 【光标功能映射】空格+方向键，映射成home end pgup pgdn
; 基础不支持三键，所以用GetKeyState实现
Space & Left::
    if GetKeyState("Shift")
        Send, +{Home}
    else
        Send, {Home}
return
Space & Right::
    if GetKeyState("Shift")
        Send, +{End}
    else
        Send, {End}
return
Space & Up::
    if GetKeyState("Shift")
        Send, +{PgUp}
    else
        Send, {PgUp}
return
Space & Down::
    if GetKeyState("Shift")
        Send, +{PgDn}
    else
        Send, {PgDn}
return

; 【快捷锁屏功能】pause锁屏，+shift休眠
Pause::DllCall("LockWorkStation")
+Pause::DllCall("PowrProf\SetSuspendState", "int", 1, "int", 0, "int", 0)

; #ifWinactive ahk_exe QQ.exe
; :*?:sd::
; s =
; (
; 13129335860
; 13129335860
; 广东省广州市白云区京溪街道京溪大街134号
; )
; paste(s)
; Return
; #IfWinActive

