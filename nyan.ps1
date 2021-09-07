$socket = New-Object System.Net.Sockets.TcpClient("nyancat.acc.umu.se", 23)
$stream = $socket.GetStream()
$reader = New-Object System.IO.StreamReader($stream)
$encoding = New-Object System.Text.AsciiEncoding
while (($line = $reader.ReadLine()) -ne $null) {
    $line.Length
}