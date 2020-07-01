#!/bin/bash

SHA1_SHORT=`git rev-parse --short HEAD`
SHA1_LONG=`git rev-parse HEAD`
COMMIT_NO=`git rev-list --count HEAD`
TIME_ISO=`git log -1 --format=%cd --date=iso8601`
TIME_ISO_STRICT=`git log -1 --format=%cd --date=iso8601-strict`
DATE=`git log -1 --format=%cd --date=short`

if [ -z "$(git status --porcelain)" ]; then
    CLEAN="clean"
    DIRTY=""
    IS_CLEAN="\\def\\VcsIsClean{}"
else
    CLEAN=""
    DIRTY="dirty"
    IS_CLEAN=""
fi

echo -e "\\def\\VcsCommitHashShort{$SHA1_SHORT}
\\def\\VcsCommitHashLong{$SHA1_LONG}
\\def\\VcsCommitNo{$COMMIT_NO}
\\def\\VcsCommitTime{$TIME_ISO}
\\def\\VcsCommitTimeISO{$TIME_ISO_STRICT}
\\def\\VcsCommitDate{$DATE}
\\def\\VcsCleanStr{$CLEAN}
\\def\\VcsDirtyStr{$DIRTY}
$IS_CLEAN
"
