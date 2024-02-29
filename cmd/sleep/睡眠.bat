@echo off
:begin
echo 请输入以下数字，确认对应操作：
echo 1.休眠
echo 2.睡眠
echo 3.重启
echo 4.关机
echo 5.滑动关机
echo 6.取消关机
echo 其他任意键退出
set /p step=
if %step% == 1 start rundll32.exe powrprof.dll,SetSuspendState 0,1,0
if %step% == 2 start rundll32.exe powrProf.dll,SetSuspendState
if %step% == 3 shutdown /r
if %step% == 4 shutdown /s
if %step% == 5 Slidetoshutdown
if %step% == 6 shutdown /a
goto begin
end