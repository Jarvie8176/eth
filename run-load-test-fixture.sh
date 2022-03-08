TEST_FIXTURE_PATH=data/test_fixture
CACHE_FILE_PATH=data/cache


mkdir -p ${TEST_FIXTURE_PATH}
wget -O ${TEST_FIXTURE_PATH}/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.txt \
  https://gist.githubusercontent.com/Jarvie8176/75a85f40cb3a9e35dd30f89b12dd5913/raw/33eec5ebc9d544a120bfb54cd706fb5193fd5254/tron_TJ7ozAvfPwxpNANWfMnAhVwGBYkwTjuscJ.txt
wget -O ${TEST_FIXTURE_PATH}/eth_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv \
  https://gist.githubusercontent.com/Jarvie8176/4fdb152d4a7815643f17dd5e7a788a77/raw/abfcc7c4158ca6489c216251a5c5f3752a82b22a/eth_0x228F5fFe4BFFE42278d50563B728aF83C36bd1A0.csv

mkdir -p ${CACHE_FILE_PATH}
wget -O ${CACHE_FILE_PATH}/eth_trx_list.txt \
  https://gist.githubusercontent.com/Jarvie8176/cb46f13b002b89dadcc38da53cce19c0/raw/0af888333a510a506b701dc2f9a27673f0c89abb/eth_trx_list.txt
