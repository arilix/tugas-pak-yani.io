import speedtest
def speedtest_internet():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert from bits to Megabits
    upload_speed = st.upload() / 10**6      # Convert from bits to Megabits
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")

speedtest_internet()
