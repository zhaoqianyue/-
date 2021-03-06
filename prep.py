# coding=utf-8
import jieba
import jieba.analyse

sentence = '信息是网络空间的基本元素，网络安全在本质上主要体现为网络信息安全。换言之，网络信息安全是网络安全的重要组成部分。没有网络信息安全，就谈不上网络安全。随着大数据及智能化技术的快速发展，网络信息安全问题日益突出，已成为全球网络治理领域的焦点和难点。顺应国内外形势变化，网络信息安全防线应在合理区间相应变动。网络信息安全防线出现畸高畸低，都将可能引发网络空间信息传播失序，进而影响互联网发展的路向及前景。安全既可表现为客观结果，又可体现为主观判断。在多元开放的网络空间，何种内容的信息应上升到“安全”的高度，继而必须采取强制干预手段？网络信息安全所指为何？对此应该做出比较清晰的研判与界定，而不能随意扩大化。否则，网络信息安全将可能成为网络信息管控的变相理由，从而导致网络信息安全防线收紧，网络信息流动受到干扰。因而，如何辩证把握网络信息安全的内涵，促使其在正当合理的范畴内得到理解与运用，是当前有待在学理层面予以剖析、澄清的一个基本问题。,\
一、网络信息安全内涵的演变随着信息技术与互联网络的迅速发展，网络信息安全的内涵不断拓展。网络信息安全是相关方使网络信息处于安全可控范围的状态和过程，以确保信息的机密性、完整性和可用性。[1]网络信息安全最初主要是指网络信息数据安全，旨在保障作为客体资源的信息数据处于合法主体的控制范围之内，不被非法窃取、删改、利用等。因为互联网最初只是一个中介化的技术装置，网络信息安全主要体现为网络数据安全。,\
由于网络社会与现实社会日益交互渗透、融合，网络空间成为国际社会展开争夺的战略资源，信息安全也由此成为互联网安全运行的首要关切。在实践及日常用语表述中，网络信息安全开始与“网络安全”和“网络空间安全”并举。[2]网络信息安全主要是指网络系统的硬件、软件及其系统数据，不遭到故意破坏、更改、泄露，系统连续可靠正常地运行，网络服务不中断。网络信息安全除了包括物理环境安全、信息系统运行安全和信息资源安全外，还应包括网络信息传播结果的安全。[3]影响网络信息传播结果的最大因素无疑是信息内容，因而网络信息传播结果安全实质所指即是网络信息内容安全。,\
从我国立法倾向来看，网络信息内容安全已成为法律规制的重点对象。我国制定首部互联网法律《全国人民代表大会常务委员会关于维护互联网安全的决定》（2000年通过，2009年修正），其主要目的就是为了“保障互联网的运行安全和信息安全”。根据该法律，有三种破坏运行安全的行为可追究刑事责任，大体可称为“侵网”、“攻网”和“断网”行为。[4]与此相比较，构成犯罪的破坏信息安全的行为共包括11种情况，侵犯客体涵盖三大类，分别为“国家安全和社会稳定”、“社会主义市场经济秩序和社会管理秩序”与“个人、法人和其他组织的人身、财产等合法权利”，如在网络空间传播有害信息煽动颠覆国家政权、利用互联网损害他人商业信誉和商品声誉及利用互联网侮辱他人或者捏造事实诽谤他人等。从中可以看出，该法律所言网络运行安全主要是指网络信息系统的稳定性与安全性，重在保障网络信息系统、设施处于正常运行状态。网络信息安全主要是指向网络信息内容安全，重在防止网络信息内容产生不良影响，引发严重后果。我国法律将“运行安全”从广义的“信息安全”中区分出来，以此能够更加凸显网络信息安全的指向性即网络信息内容安全。,\
全国人民代表大会常务委员会颁布施行《关于加强网络信息保护的决定》（2012年通过），首要目的同样是“为了保护网络信息安全”。该法律重在保护网络个人信息安全（主要包括能够识别公民个人身份和涉及个人隐私的两类信息），同时要求网络服务提供者加强对其用户发布信息的管理，一旦发现法律法规禁止发布或者传输的信息，应当立即停止传输、采取消除等处置措施。显然，该法律所保护的网络信息安全同样包括网络信息内容安全，旨在调试网络空间中信息与个人、社会和国家之间的关系结构，其中关键因素是对于信息内容安全系数的认定。在一些刑事案件的判决文书中，保护网络信息安全亦成为较为常见的判决理由。例如，在“王欣等传播淫秽物品牟利案”（俗称“快播案”）中，快播公司被判罪处罚是因其未尽管理义务而导致淫秽视频大量传播，这被审判法院归为“网络信息安全问题”。[5]此处的网络信息安全，显然是指网络信息内容安全。,\
由此可见，网络信息安全的内涵已从物理与技术属性的“硬安全”向媒介属性的“软安全”延伸。这并不是说后者的重要程度要高于前者，而只是表明相比于前者，网络信息内容安全已成为网络信息安全日益关切的常态化问题，也是更为棘手的问题。当前，网络信息内容安全已成为国家信息安全保障体系的重要组成部分，是管理网络信息传播的重要手段，对维护国家和社会长治久安具有重要意义'

keywords = jieba.analyse.extract_tags(sentence,topK=20,withWeight=True,allowPOS=('n','nr','ns'))

for items in keywords:
	print(items[0],items[1])