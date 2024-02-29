; 粘贴字符串
paste(s) {
    Clipboard := s
    Send, ^v
}