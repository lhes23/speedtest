import speedtest

test = speedtest.Speedtest()

down_speed = test.download() / 1024 / 1024
up_speed = test.upload() / 1024 / 1024

print(f"Download: {down_speed:.2f} mbps")
print(f"Upload:  {up_speed:.2f} mbps")