import requests
import urllib3
import time
urllib3.disable_warnings()
response = requests.get('https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200fc80000beb5rlqgd9ft9jma9lkg&line=0',verify=False)

size = 0
chunk_size = 1024
counter = 1
with open(r'urlsfile.txt') as urlsfile:
    while True:
        url = urlsfile.readline()
        if not url:
            break

        try:
            response = requests.get(
                url,
                verify=False)
            filename = 'cailuoli/'+ str(int( time.time())) + '.mp4'
            with open(filename, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    file.flush()
            print('finish='+str(counter))
            counter = counter + 1
        except Exception as e:
            print(e)
    # print(url+" ")



# with open(r'douyinsss.mp4', "wb") as file:
#     for data in response.iter_content(chunk_size=chunk_size):
#         file.write(data)
#         size += len(data)
#         file.flush()