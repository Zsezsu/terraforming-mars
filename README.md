# Terraforming Mars

## About

This application is based on the famous game **Terraforming Mars**.

In Terraforming Mars, you play a corporation sponsored by the World Government on Earth, in the 2400s. Launch ambitious
Mars terraforming projects such as increasing the temperature, oxygen level, creating oceans, forests and more. In the
face of rival corporations, make the biggest contribution by building infrastructure and making the planet habitable,
and win the race to terraform!

## GIT Guidelines

### Commits

**Commit frequently.**
Don't worry about whether your change will go into the final branch version or not, you can manipulate commits with
several git rebase methods (such as squash). The important thing here is to commit very often.

Commit message examples:

`Add login system`

`Fix input bug`

`Update tiles`

### Branching

Don't commit directly to the development branch. Create **[ feature | enhancement | fix ]** branches to record your
changes.

Name the branches as the following:

`git branch <github-username>_<branch-type>_<branch-name>`

### Rebase

Do the following when rebasing a branch to the development.

1. On **development** branch `git pull`
2. On **custom branch**
    - `git pull`
    - `git rebase -i development`
3. Finish rebase by resolving merge conflicts if necessary.
    1. After resolving conflicts, `git rebase --continue`
4. Check if the application works as it should
5. Complete rebase by `git push -f`
