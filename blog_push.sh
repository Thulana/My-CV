#!/bin/sh


commit_website_files() {
  git clone https://github.com/Thulana/thulana.github.io.git
  cp ./cv.pdf ./thulana.github.io/assets/cv.pdf
  cd ./thulana.github.io && git add assets/cv.pdf
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER - Pushing updated cv to the blog"
#  git push https://"${GITHUB_USER}":"${GITHUB_PASSWORD}"@thulana.github.io.git --all
  git push origin master
}


echo "pushing to my blog"
commit_website_files
#upload_files
