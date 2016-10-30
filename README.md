# What

Proxies a number of back end http servers with a single basic auth password and nice login landing page.  This is for internal servers for small companies without SSO.

# How to use

1. Make sure all services are only accessible from the proxy, probably via docker routing.
2. Run
```
TITLE="My Services" PASSWORD=password SERVERS='[["server1", 8081, 9165]]' docker run baxter/basic-auth-landing
```
replacing `TITLE`, `PASSWORD`, and `SERVERS`.  `SERVERS` is a json-encoded array of 3-tuple arrays of the service name, the exposed port, and the internal port.
