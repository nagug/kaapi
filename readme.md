# Kaapi nginx installer (Not ready for use - work in progress)

Kaapi is a python based custom nginx installer for debian systems focussed on having all security & performance module integrated. Unlike other systems, kaapi builds the nginx from source. 

**Tip!** You need sudo access to run kaapi

**Is Kaapi ready to be used?** NO. This is still work in progress.

## Kaapi Magic
***
Kaapi Magic provides you the option to install all the pre-defined modules. The command is invoked by

```
sudo kaapi magic
```

This builds installs the latest version of all of these

**nginx**
* mainline nginx

**Security module**
* Naxsi WAF
* LibreSSL

**Performance modules**
* ngx_pagespeed
* ngx_brotli
* cloudflare TLS dynamic patch

**Other**
* ngx_headers_more

**Hint :** Please feel free to suggest any additional module to be added.

## Kaapi Customisation options
***
Kaapi provides way to customise the installation. Following options are available. Adding any of these flags will trigger customisation.

### --no-xxx approach

**Example**
```
sudo kaapi --no-pagespeed
```

This removes pagespeed from the over all build. Available options are
* no-pagespeed
* no-naxsi
* no-tlspatch
* no-brotli
* no-libressl

Options can be stacked like any other linux commands

**Example**
```
sudo kaapi --no-pagespeed --no-naxsi
```

Above command installs everything except pagespeed and naxsi.

### --add-xxx approach

**Example**
```
sudo kaapi --add-pagespeed --add-naxsi
```

This alternate approach is handy, if the intention is to install only minimal options over mainline nginx. The above example installs mainline nginx, pagespeed and naxsi.

### Mixing and matching approaches
It is not expected to mixing and matching the approaches. However in such a scenario, the behaviour will be as below.

**Example**
```
sudo kaapi --no-naxsi --add-naxsi 
```

The above command triggers customisation mode and will simply install mainline version. No other module will be installed

**Example**
```
sudo kaapi --no-naxsi --add-naxsi --add-pagespeed
```

The above command triggers customisation mode and will install mainline version along with pagespeed module.

**Example**
```
sudo kaapi --no-naxsi --add-naxsi --no-pagespeed
```

The above command triggers customisation mode. However, since there are no --add flags, This will install magic version except pagespeed.

**Example**
```
sudo kaapi --no-naxsi --add-naxsi --no-pagespeed --add-tlspatch
```

The above command triggers customisation mode. since there is a --add flag, mainline version along with tlspatch will be installed.

## FAQs

1. What is Kaapi means?
Kaapi is South Indian variation of coffee. For some para-normal reason, it has helped me whenever, I had Migraines. No medical explanation yet.
2. Why this project?
Bored of typing too many commands, everytime I setup a server. Also since my day job does not let me code, these kind of projects keeps me engaged in the night.