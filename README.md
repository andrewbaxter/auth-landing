# What

Proxies a number of back end http servers with a single basic auth password and nice login landing page.  This is for internal servers for small companies without SSO.

# How to use

1. Make sure all services are only accessible from the proxy, probably via docker routing.
2. Generate an SLL cert and key with:
```
mkdir ssl
cd ssl
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```
3. Run
```
docker run -e -e PASSWORD=password -e SERVERS='[["server1", 8081, 9165]]' -p 8081:8081 -v `pwd`/ssl:/etc/ssl:ro baxter/basic-auth-landing
```
replacing `PASSWORD`, and `SERVERS`.  `SERVERS` is a json-encoded array of 3-tuple arrays of the service name, the exposed port, and the internal port.  Each exposed port must also be added with `-p`.
