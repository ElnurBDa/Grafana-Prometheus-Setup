```bash
# setup certificates
cd ~/monitoring/ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout selfsigned.key -out selfsigned.crt \
  -subj "/C=US/ST=State/L=City/O=Organization/OU=IT Department/CN=yourdomain.com"

# give proper permissions
sudo chown -R 472:472 grafana
sudo chown -R 65534:65534 prometheus
sudo chmod -R 755 ssl

# setup password in prometheus/web.yml
python3 enc-pass.py

# add to /etc/docker/daemon.json and restart docker
{
  "metrics-addr": "0.0.0.0:9323",
  "experimental": true
}

# run
docker compose up -d
```
