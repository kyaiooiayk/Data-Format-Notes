echo "PR and merge into main!"
git add .
git commit -m "_"
git push --set-upstream origin dev
gh pr create -B main -H dev -f
gh pr merge --admin -m
echo "All done!"
