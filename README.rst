Magical Diet Recipe Directory
#############################

This is a flask + bootstrap demo application with dockerisation features to use as a fun example of deployments. The magical diet? You mindfully look at empty plates, but only the plates sold by the influencer who invented it ... *(hopefully the sarcasm is obvious, it's an imaginary application and no influencers were harmed in the making of this demo)*.

Set up the application
======================

Flask expects the `PG_URI` environment variable to be present and hold a connection string for a postgres database.

Build the image:

```
docker build -t flaskapp .
```

Then spin up a container:

```
docker run --rm -v /path/to/your/dir/:/app --name myflask flaskapp --env PG_URI="[paste from aiven web interface]"
```



