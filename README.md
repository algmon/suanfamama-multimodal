![](./img/cover.png)

## 当前研究课题：多模态内容感知、生成及个性化创意应用场景研究
## 当前理论框架依据：认知计算广告
## 子课题
### 子课题及论文题目（拟） - 1 - “AIGC内容创意工作流”在垂直领域的应用
* paper 1 - workflow.md
* 关键词及着眼点：工作流
* 写作思路：从基本工作流过渡到分布式协同工作流
* 基于认知计算广告理论，进一步提出了分布式协同工作流、基于节点的编排、低代码等核心技术的落地应用，并以时尚行业设计师工作流为例，加以验证。
* 创新点及难点：如何设计分布式协同工作流 及 分布式协同工作流在垂直领域的应用
* 案例1：如何使用 linkai 构建营销工作流？
* 案例2：省广集团是如何有效使用工作流及协同功能以降本增效？
* 案例3：在广告创意垂类中如何解决分布式协同问题？
* 案例4：智能营销洞察
  * 步骤1：对数据进行分析洞察
  * 步骤2：获得消费者反馈，丰富顾客画像
  * 步骤3：优化营销运营策略
  * 步骤1-3 不断迭代
* 案例5：生成式AI的多模态内容生成
  * 线性前置步骤：创意确定
    * 并行步骤: 文本
    * 并行步骤: 图片
    * 并行步骤: 声音
    * 并行步骤: 视频
    * 并行步骤: 代码
  * 线性后置步骤：人工审核
* TODO1：清楚定义什么叫分布式协同工作流
* TODO2：使用数字签名是否能有效防止工作流被篡改？
* 所投期刊 新闻与传播 TODO: 未确定

### 子课题及论文题目（拟） - 2 - “AIGC内容创意知识库”在垂直领域的应用
* paper 2 - kb.md
* 关键词及着眼点：知识库
* 写作思路：从基本单一知识库到多模态AIGC创意知识库
* 基于认知计算广告理论，进一步系统阐明在实际生产应用中，如何综合使用关系型、非关系型，对象及新型向量数据库以构筑垂类AIGC知识库供下游应用调用。
* 创新点1：多模态AIGC创意知识库
* 创新点2：AIGC创意知识库是如何把 元认知知识、概念性知识、程序性知识及技能性知识整理、归纳并融合在一起的
* 案例1：如何使用dify平台构建多模态AIGC创意知识库
* 案例2：如何使用coze平台构建多模态AIGC创意知识库
* 所投期刊：新闻与传播如 TODO: 未确定

### 子课题及论文题目（拟） - 3 - “AIGC内容创意垂类模型"在垂直领域的应用
* paper 3 - model.md
* 关键词及着眼点：垂类模型
* 写作思路：使用RAG技术使生文通用模型足够垂类，使用微调技术使生图通用模型足够垂类。
* 基于认知计算广告理论，着眼于于垂类大模型RAG（生文模型）、微调（生图、生视频模型）等技术，系统阐明如何高效挖掘新知识，使通用知识大模型插上垂类翅膀，并提及提示词工程及智能词元（token）生成，即大模型是通过什么架构去处理多模态的输入及输出的。
* 创新点：（暂无，RAG及微调技术是目前业界已有标准技术）
* 案例1：如何使用“通用生文大模型 + RAG“做带有风格的时尚内容创作（文本）
* 案例2：如何使用“通用生图大模型 + 微调”做带有风格的时尚内容创作（图片）
* 案例3：如何使用“通用生视频大模型 + 微调”做带有风格的时尚内容创作（视频）
* 所投期刊：新闻与传播如 TODO: 未确定

### 子课题及论文题目（拟） - 4 - “AIGC内容创意智能体”在垂类场景中的应用
* paper 4 - scene.md
* 关键词及着眼点：“创意型智能体”、“垂直落地场景”
* 写作思路：在开篇给出智能体的定义及行动流程，即环境交互 -> 感知信息 -> 思考 -> 采取行动。由客户需求倒推如何设计落地场景及相关智能体，并且在设计与实现智能体过程中要非常重视智能体的价值对齐问题，写作过程中需强调人机协作，强调目前智能体能达到一定的智能推理能力，但尚不够。
* 基于认知计算广告理论，进一步提出在不同垂直场景及细分需求下的技术选型，以满足客户需求。
* 创新点1：不强调 使用智能体以降本增效，强调 使用智能体以提升内容创作及灵感获取能力
* 创新点2：强调 提示词工程、知识库、分数的“融合微调”核心技术（案例：如何在实际工程中价值对齐一个时尚买手智能体的音容相貌乃至部分时尚大脑职能）
* 难点：多智能体如何协作与感知？如何有效从个体智能到群体智能？
* TODO: 案例1：如何设计一个智能体，她的目标是提升广告投放效果？
* TODO: 案例2：如何设计一个智能体，她的目标是输出源源不断的创意及灵感？
* TODO: 案例3：如何设计一个时尚买手智能体，她的目标是对人群或个体时尚进行评价，评分并作搭配推荐
* TODO: 案例4：华为HAS 2024 AIGC 宣传视频
* TODO: 实验设计：如何设计一个智能体，做落地应用场景相匹配决策（决策如智能排期）。如此广告在此刻是否生成，此广告是否投放在某个用户的折扣圈中？
* 所投会议：计算机科学如 SIGIR, CIKM et. al.

## 相关工作
### 1. 计算广告
（写作思路：根据计算广告逻辑演进框图重新表意）
计算广告是利用计算机技术对广告投放进行优化、定制和智能化,以提高广告的精准投放和效果的一种广告模式【1】。它是互联网广告发展的重要形式,成为各大互联网公司的核心收入来源【2】。计算广告经历了以下3个主要发展阶段【6】。（1）1.0 时代: 程序化广告,基于简单数学模型,以文字广告为主,通过竞价排名等机制进行广告投放,如Google、百度的广告系统；（2）2.0 时代: 智能推荐广告,对用户画像和广告特征进行更精细的分析,在广告智能投放和效果付费方面有长足进步,如微信朋友圈、抖音等的智能广告投放；（3）3.0 时代: 认知计算广告,以AI技术为基础,以AIGC为逻辑,以认知科学为理论,重点解决广告创意生成等问题,利用多模态垂类模型生成文字、图片、视频等广告内容。
TODO: 补充 1.0 时代的 Google Ads，以搜索作为核心业务下的广告业务
TODO: 补充 2.0 时代的 Meta Ads，以社交为核心业务下的广告业务
TODO: 强调 在 3.0 时代，以AIGC内容创意作为核心的相关行业领导者 尚未 出现

### 2. 中国认知计算广告知识体系
认知计算广告的理论体系诞生于2024，由段淳林及其研究团队首先提出，在【10】中有对其理论体系发展脉络的系统性论述。其中，类思维，智能体社交及价值对齐是三个核心营销概念。类思维【】是指智能体通过分类、归纳等认知过程,对事物进行抽象和概括,从而达到对复杂环境的理解和预测。这种类概念思维是智能体社交的基础,帮助智能体快速感知外界,并做出相应的反应。智能体社交【】指智能体之间基于类思维进行信息交互和行为协调的过程。不同的智能体可以通过交流与协作,共享知识和经验,实现目标的达成。这种社交互动是智能系统发展的关键。价值对齐【】是指智能体内部price和reward等价值系统,以及智能体之间的目标价值趋同。当智能体内部价值系统和外部环境的价值目标达成一致时,就实现了价值对齐。这是智能体最终实现高度自主和协同的基础。
TODO: 补充 阿诺德 认知-情感-意动 模型

理论外延在众多学者的共同努力下得到较好扩展。在【7】中，段淳林及魏方等在此核心理论下进一步率先提出基于认知计算广告的研究范式。在【8】中，段淳林及陆昊琪等在此核心理论下进一步率先提出基于认知计算广告的生产范式。在【9】中，段淳林及蒲源等在此核心理论下通过量化实验方法，融合深度神经网络等AIGC技术，使用领域数据训练了一个广告传播力预测模型，并使用B站大数据进行了可行性分析及原型验证。实验表明，此广告传播力预测模型能准确预测B站上某条广告或视频的传播力和影响力。

### 3. 基于认知计算广告的多模态内容感知、生成及个性化创意应用研究
如【11】中，段淳林及江纬等基于认知计算广告理论，进一步提出了分布式协同工作流、基于节点的编排、低代码等核心技术的落地应用，并以时尚行业设计师工作流为例，加以验证。在【12】中，段淳林及江纬等基于认知计算广告理论，进一步系统阐明在实际生产应用中，如何综合使用关系型、非关系型，对象及新型向量数据库以构筑垂类AIGC知识库。核心待解决问题是如何对知识进行收集、整理、加工及存储，以使得更好的搜索、推荐及数据挖掘。在【13】中，段淳林及江纬等基于认知计算广告理论，着眼于于垂类大模型的RAG、微调等算法技术，系统阐明如何高效和挖掘新知识，并与所选基模型形成互补。作者进一步阐明了如何在垂类行业如时尚中去灵活使用不同的大模型、RAG及微调等方法，以满足既定评价指标。在【14】中，段淳林及江纬等基于认知计算广告理论，进一步提出在不同垂直场景及细分需求下的技术选型，以满足客户需求。

## 参考文献
### 论文
1. 段淳林,任静等.智能广告的程序化创意及其RECM模式研究[J].新闻大学,2020(2):17-31 + 119-120
2. 段淳林,杨恒等.数据、模型与决策:计算广告的发展与流变[J].新闻大学,2018(1):128-136 + 154
3. 段淳林,宋成等.用户需求、算法推荐与场景匹配:智能广告的理论逻辑与实践思考[J].现代传播.2020,42(8):199-128
4. 段淳林,崔钰婷等.计算广告学科建设持续创新能力的影响研究——组织学习与知识共享的链式中介效应分析[J].现代传播.2024年第三期
5. 段淳林,周学琴等.虚拟主播的形象行为相似性对消费者品牌信任的影响研究——基于临场感的中介效应[J].（在这篇论文中，研究团队揭示了虚拟主播的形象和行为相似性在提升消费者品牌信任中的作用，特别是临场感在此过程中扮演的重要角色。）
6. 段淳林等.生成式AI营销中的三个核心概念.20240628
7. 段淳林,魏方等.（关于认知计算广告研究范式）.2024（在投中）
8. 段淳林,陆昊琪等.（关于认知计算广告认知计算广告知识生产范式）.2024（在投中）
9. 段淳林,蒲源等.（关于认知计算广告及使用B站数据所做的实验及模型）.2024（在投中）
10. 段淳林等.（关于认知计算广告蓝皮书）.华南理工大学.2024（撰写中）
11. TODO 段淳林,江纬等.AIGC创意工作流.workflow -
12. TODO 段淳林,江纬等.AIGC创意知识库.kb -
13. TODO 段淳林,江纬等.AIGC创意模型.model -
14. TODO 段淳林,江纬等.AIGC创意场景.scene -
15. TODO 类思维【】
16. TODO 智能体社交【】
17. TODO 价值对齐【】

### 教科书
1. 段淳林.计算广告学导论[M].武汉:华中科技大学出版社,2022
2. 刘鹏,王超.计算广告:互联网商业变现的市场与技术[M].3版.北京:人民邮电出版社,2022
3. 段淳林.整合品牌传播:从IMC到IBC理论建构[M].北京:人民出版社,2020
4. 陈刚等.创意传播管理:数字时代的营销革命[M].北京:机械工业出版社,2012
5. BISHOP C M. Pattern Recognition and Machine Learning. Springer[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI), 2006, 16(4):049901
6. TODO ARENSW.当代广告学[M].丁俊杰,程坪,译.北京:人民邮电出版社,2005

### 相关学术研讨会
1. 生成式AI与跨学科融合：机遇、挑战与应对.华南理工大学.20240613

## TODO:
1. 迭代 文献梳理（关注（1）国际计算广告发展（2）中国认知计算广告体系构建（3）最（较）前沿AIGC创意生成技术）
2. 设计 实验
3. 撰写 若干篇小论文

## 现存问题
1. TODO: 在哪里强调智能体与真人的情感链接较为合适？
2. TODO: 如何体现个性化服务？
3. 把以下趋势融入到小论文的写作中
* 趋势1：从数据驱动到知识库生成成为认知计算广告的新范式
* 趋势2：人机协同的文本交互是认知计算广告主体性演变的新载体
* 趋势3：多模态内容感知与生成成为认知计算广告创意新引擎
* 趋势4：AIGC+产业成为未来超级商业体的新风口
* 趋势5：从程序化Agent到代理化Agentic是通向AGI的发展之路
* 趋势6：构建基于中国实践的认知计算广告自主知识体系与理论创新

## 术语
1. 生成式AI
2. AIGC创意
3. 提示词工程
4. 感知
5. 认知
6. 生成
7. 推理
8. 传播
9. 框架
10. 垂直化场景
    * 即垂类场景
11. AGI
12. 协作
13. 人人协作
14. 机机协作
15. 人机协作
16. 智能体 AI Agent
17. 思维传播框架
18. 内容运营与管理
19. 多模态
20. AI工具
21. 知识库
   * 元认知知识
   * 概念性知识
   * 程序性知识
   * 技能性知识
22. 内容银行
   * 内容银行是把内容看作是和金钱一样可以存储的资产，运营和管理内容资产（源：段淳林等）
