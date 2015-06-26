#computational-project-cookie-cutter
A cookie cutter (aka project template) to set up a folder structure for a computational project.
This is a quick way to setup a folder structure that follows one standard to organize a project.
This helps with project management, reproducibility, sharing, and publishing your data, analysis, and results.

This project was inspired (and modeled off) by:

[Noble WS 2009 A Quick Guide to Organizing Computational Biology Projects. PLoS Comput Biol 5 7: e1000424. doi:10.1371/journal.pcbi.1000424](http://dx.doi.org/10.1371/journal.pcbi.1000424)

## What it does
the `setup_project_dir.sh` script creates the following folder structure:

    Path_Provided
    |- doc/           # directory for documentation, one subdirectory for manuscript
    |
    |- data/          # data for storing fixed data sets
    |
    |- src/           # any source code
    |
    |- bin/           # any compiled binaries or scripts
    |
    |- results/       # output for tracking computational experiments performed on data

A README containing a brief blurb is placed in each folder.
This is because git will not track empty folders and placing a README will
remind you of what goes in each folder, and also the overall
folder structure will be retained

If you use a webservice in conjunction with your version control (e.g. github, bitbucket, gitlabs, gitbucket, etc)
the webservice will be able to render these README and other [markdown](https://help.github.com/articles/markdown-basics/) files automatically.

This project was taken from [this](https://github.com/chendaniely/computational-project-cookie-cutter) github repo
