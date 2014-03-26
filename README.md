Evolve Package Repository
=========================


Versioning and Specifics
------------------------

Evolve versioning uses the following scheme:


```
MAJOR.YYYYWW.DD.BUILD

```

All changes should initially be made to the `develop` branch, enabling us to
maintain a static master for the majority of the time. If today's date is
the 12th of September, 2013, we can say that our base version number would be:

    2.201337.4.0

Once packages have survived testing in `develop`, they can then be merged into
master. A new version number does not need to be generated unless a build has
been queued, which will push the packages into the public binary repositories.

At this point, a new tag with the current version number should be created and
pushed to the repository, and a `ChangeLog` should accompany this tag, listing all
changes between this tag and the last. This enables real tracking of the repository
between different releases, and different upgrades. Using the date system also
enables us to quickly identify exactly which update caused any issue.


Build number is used to accomodate multiple builds in one day, and may be omitted for the
first build. Subsequent releases on the same day should start their build number at 1,
and increment from there. If a new queue was released on the same day, it could have the
version:

    2.201337.4.1

Shortening versions
-------------------

During the current working year it may sometimes be appropriate to commonly refer to versions
without using the ISO year, especially for conversational uses. Official publications will always
refer to the full EvolveOS version number for the sake of professionalism.

To use the above version numbers as an example, a user may refer to an update as:

    2.37.4.1

Helpful commit messages
-----------------------
In time many changelogs will be generated using automated tools, to determine if version numbering
is correct, and to asssociate the correct tags. In order to help with this your commit message
must now *always* be appropriately prefixed with one of the following:

 * [NEW] indicates a new package being added to the repo
 * [UPDATE] indicates a package upgrade
 * [FIX] indicates a security or bugfix
 * [REMOVE] used to remove a package from the repository
 
Authors
-------

 * Ikey Doherty <ikey@solusos.com>
