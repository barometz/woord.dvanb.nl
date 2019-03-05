Title: Certbot/Let's Encrypt renewal + Lighttpd
Slug: certbot-lighty-renewal
Tags: web, software
Category: Computer Tech
Lang: en
Status: published

Something very small I finally fixed today: [Certbot](https://certbot.eff.org/), the tool to get [Let's Encrypt](https://letsencrypt.org) SSL/TLS certificates, doesn't support the [lighttpd](https://lighttpd.net) webserver. For some other webservers it can automatically deploy its output and restart the server, but not for lighty. It *does* automatically renew the certificates every so often, but that doesn't do much good without copying over the files.

Fortunately certbot does have a flag to do whatever you want for deployment:

```man
    --deploy-hook DEPLOY_HOOK
                            Command to be run in a shell once for each
                            successfully issued certificate. For this command, the
                            shell variable $RENEWED_LINEAGE will point to the
                            config live subdirectory (for example,
                            "/etc/letsencrypt/live/example.com") containing the
                            new certificates and keys; the shell variable
                            $RENEWED_DOMAINS will contain a space-delimited list
                            of renewed certificate domains (for example,
                            "example.com www.example.com" (default: None)
```

And so, assuming you keep your certificates in `/etc/lighttpd/certificate/your.host.name.pem`:

```sh
#!/usr/bin/env bash

# -e causes the script to exit when any command fails; -u makes undefined
# variable expansions a failure.
set -eu

if [ "$EUID" -ne 0 ]; then
    echo  "Please run as root"
    exit 1
fi

# Get the domain name from the RENEWED_LINEAGE env var
domain=$(basename $RENEWED_LINEAGE)
# Copy the two certificate files to lighty's preferred single-file format
cat $RENEWED_LINEAGE/privkey.pem $RENEWED_LINEAGE/cert.pem \
  > /etc/lighttpd/certificate/$domain.pem
# The full chain is identical between all certs
cp $RENEWED_LINEAGE/fullchain.pem /etc/lighttpd/certificate/

systemctl restart lighttpd
```

Run `certbot [run, renew] --deploy-hook /path/to/lighty-cert-deploy.sh` and you're set. The deployment hook is added to certbot's auto-renewal configuration as well, so you can forget about it forever.
