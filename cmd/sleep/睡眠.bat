@echo off
:begin
echo �������������֣�ȷ�϶�Ӧ������
echo 1.����
echo 2.˯��
echo 3.����
echo 4.�ػ�
echo 5.�����ػ�
echo 6.ȡ���ػ�
echo ����������˳�
set /p step=
if %step% == 1 start rundll32.exe powrprof.dll,SetSuspendState 0,1,0
if %step% == 2 start rundll32.exe powrProf.dll,SetSuspendState
if %step% == 3 shutdown /r
if %step% == 4 shutdown /s
if %step% == 5 Slidetoshutdown
if %step% == 6 shutdown /a
goto begin
end