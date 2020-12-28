#!/bin/bash

./rdb/make_rdb.sh

cd ./HsqlDBembeddedOOo/
zip -0 HsqlDBembeddedOOo.zip mimetype
zip -r HsqlDBembeddedOOo.zip *
cd ..

mv ./HsqlDBembeddedOOo/HsqlDBembeddedOOo.zip ./HsqlDBembeddedOOo.oxt
