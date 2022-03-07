TEST_FIXTURE_PATH=data/test_fixture


if [ -d ${TEST_FIXTURE_PATH} ]; then
  echo "test fixture path already exists"
  exit 0
fi

mkdir -p ${TEST_FIXTURE_PATH}

wget -O ${TEST_FIXTURE_PATH}/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.txt \
  https://gist.githubusercontent.com/Jarvie8176/75a85f40cb3a9e35dd30f89b12dd5913/raw/33eec5ebc9d544a120bfb54cd706fb5193fd5254/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.txt
