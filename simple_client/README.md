# MOTD service

### Note:
- Collect **`message book`**
- features: Display **`date/language/Add new message`**
- architecture
- required skills
- simple http server can't change index.html, so **cron job** will be used to update the file
  - `crontab -e`
  - `0 6,12 * * * /home/newton.lee/work/github/pyal/simple_client/motd/motd.py`

### How-to:
- Run **`server.py`** first.
- Now, run **`client.py`**.
- verify the output.

### Problems I met
- While working on https://webisfree.com/2019-11-19/python-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%9B%B9%EC%84%9C%EB%B2%84-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-simple-web-server
- Can't run daemon in **`background`**
- when run for the second time, got error **`OSError: [Errno 98] Address already in use`**
- **`python -m http.server 8080`** (since 3.0) seems to be great



