#!/bin/sh

commit_website_files() {
  cp ./cv.pdf ./blog/assets/cv.pdf
  cd ./blog && git add assets/cv.pdf
  git config user.name github-actions
  git config user.email github-actions@github.com
  git commit --message "Commit: $SHA8 - Pushing updated cv to the blog"
  git push
}


echo "pushing to my blog"
commit_website_files
