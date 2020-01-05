#!/bin/sh

setup_git() {
  git config --global user.email "${GITHUB_EMAIL}"
  git config --global user.name "${GITHUB_USER}"
}

commit_website_files() {
  git clone https://github.com/Thulana/thulana.github.io.git
  cp ./cv.pdf ./thulana.github.io/assets/cv.pdf
  cd ./thulana.github.io && git add assets/cv.pdf
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER - Pushing updated cv to the blog"
#  git push https://"${GITHUB_USER}":"${GITHUB_PASSWORD}"@thulana.github.io.git --all
  git push https://"${GH_TOKEN}"@github.com/Thulana/thulana.github.io.git master
}


echo "pushing to my blog"
setup_git
commit_website_files
#upload_files
