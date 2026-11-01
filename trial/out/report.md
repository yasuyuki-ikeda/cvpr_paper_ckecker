# 要約の試験結果

| 方式 | 言語 | 1 本あたり | モデル読み込み | 形式どおりの答え |
|---|---|---|---|---|
| extractive | en | 0 秒 | - 秒 | 20/20 |
| q25-1.5b.gguf | en | 8.2 秒 | 2.0 秒 | 20/20 |
| q25-1.5b.gguf | ja | 7.9 秒 | 2.0 秒 | 20/20 |
| q25-3b.gguf | en | 14.4 秒 | 3.0 秒 | 20/20 |
| q25-3b.gguf | ja | 16.6 秒 | 3.0 秒 | 20/20 |
| q3-1.7b.gguf | en | 12.3 秒 | 1.0 秒 | 20/20 |
| q3-1.7b.gguf | ja | 13.2 秒 | 1.0 秒 | 20/20 |
| q3-4b.gguf | en | 22.3 秒 | 3.0 秒 | 20/20 |

## 1. Latent Space Jam: Layout Guided Video Synthesis

https://arxiv.org/abs/2610.30390

<details><summary>要旨（原文）</summary>

Adding control to video generation often requires training, which demands additional computational resources, data, or architectural changes. We propose a training-free approach that utilizes pretrained video diffusion models to control object layout and motion using coarse layouts. Our method operates in two passes: first, it steers spatiotemporal placement through prompt-guided cross-attention to produce a coarse visual guide; second, this guide conditions the same model to generate a high-quality, layoutconsistent video. The approach enables coordinated motion with strong temporal consistency, supporting diverse trajectories and object interactions without additional training. Extensive experiments show that our method consistently outperforms prior work in overlap and trajectory accuracy, as well as visual quality across static, dynamic, and multi-object scene settings.

</details>

**extractive / en**

- 【課題】ビデオ生成に制御を追加するには、多くの場合、トレーニングが必要であり、追加の計算リソース、データ、またはアーキテクチャの変更が必要です。
- 【方法】粗いレイアウトを用いて物体のレイアウトと運動を制御するために，事前訓練されたビデオ拡散モデルを利用する訓練なしのアプローチを提案した。
- 【従来からの進化】広範な実験は、我々の方法は一貫して静的、動的、およびマルチオブジェクトシーン設定全体の視覚的な品質だけでなく、重複と軌道精度で以前の作業を優

**q25-1.5b.gguf / en**（8.4 秒）

- 【課題】ビデオ合成におけるオブジェクトのレイアウトと動きを制御するためのトレーニングフリーのアプローチ
- 【方法】事前学習されたビデオ拡散モデルを使用して、時空間的な配置を操縦し、レイアウト一貫性のあるビデオを生成します
- 【従来からの進化】強力な時間的一貫性を持つ協調運動を可能にし、追加のトレーニングなしで多様な軌道とオブジェクトの相互作用をサポートすることによ

**q25-1.5b.gguf / ja**（6.9 秒）

- 【課題】视频生成中控制物体布局和运动需要额外的计算资源、数据或架构变化
- 【方法】提出一个无需训练的方法，利用预训练的视频扩散模型控制物体布局和运动
- 【従来からの進化】无需额外训练，通过粗布局引导生成粗视觉指南，再使用该指南条件生成高质量、布局一致的视频

**q25-3b.gguf / en**（13.3 秒）

- 【課題】ビデオ生成に制御を追加するには、追加のリソースまたはアーキテクチャの変更が必要です。
- 【方法】粗い視覚ガイドを通じて、事前学習済みのビデオ拡散モデルを用いてレイアウトと動きを制御する、トレーニング不要のアプローチです。
- 【従来からの進化】一貫して重複および弾道の正確さ、設定を渡る視覚質の前の仕事に優っています。

**q25-3b.gguf / ja**（13.5 秒）

- 【課題】既存手法は訓練が必要で資源を消費する。
- 【方法】予測済み動画差分モデルを用いて、粗いレイアウトと動きを制御する。
- 【従来からの進化】強力な時系列的一貫性と多様な軌跡をサポートする。

**q3-1.7b.gguf / en**（9.9 秒）

- 【課題】トレーニング-オブジェクトレイアウトコントロールを使用した無料のビデオ生成は困難です。
- 【方法】粗いレイアウトで事前学習されたビデオ拡散モデルを使用して、時空間的な配置と動きをガイドします。
- 【従来からの進化】20%のより高い弾道の正確さおよび30%のよりよい視覚質のレイアウトの一貫性および動きの一貫性を改善する。

**q3-1.7b.gguf / ja**（13.1 秒）

- 【課題】既存手法では、ビデオ生成に制御を加えるためのトレーニングが必要で、計算リソースやデータが必要である。
- 【方法】訓練なしで、事前学習した動画差分モデルを用いて、コアーレイアウトを基に動画生成を行う。
- 【従来からの進化】時空間配置を促進し、高品質な動画生成を実現。

**q3-4b.gguf / en**（17.1 秒）

- 【課題】既存のビデオ生成方法ではトレーニングが必要であり、計算コストとデータコストが高くなります。
- 【方法】粗いレイアウトでオブジェクトのレイアウトと動きを制御するために、事前に訓練されたビデオ拡散モデルを使用し
- 【従来からの進化】複数のシーン設定にわたるオーバーラップ、軌跡の精度、視覚的品質において、以前の作業よりも優れています。

## 2. A Visual Grounding Benchmark for Retinal OCT with Multimodal Large Language Models

https://arxiv.org/abs/2610.31205

<details><summary>要旨（原文）</summary>

Multimodal large language models (MLLMs) can answer clinical questions about medical images, but trustworthy use requires visual grounding: models should localize the pathology they report rather than rely on spurious shortcuts. Whether MLLMs can visually ground clinical findings in retinal optical coherence tomography (OCT), the most widely used imaging modality in ophthalmology, remains largely unexplored. To address this gap, we introduce RetinaGroundBench, the first benchmark for biomarker visual grounding in retinal OCT. It comprises 815 B-scans exhaustively annotated by ophthalmologists with 4,537 bounding boxes covering 13 biomarkers across 8 diseases. Because MLLMs often fragment a single lesion into multiple partial predictions, we propose AggIoU, a metric that evaluates whether the union of overlapping predicted boxes covers the annotated region. Across 27 open-source MLLMs (0.8-38B parameters), we find that visual grounding remains largely unsolved: the best general-purpose model achieves a macro F1 of just 23.7%, with consistently low recall, despite reaching up to 73% balanced accuracy on biomarker presence questions. To narrow this gap, we developed RetGrounder, an MLLM fine-tuned using an OCT-specific strategy integrating grounding and textual information. Despite its relatively small size (8B), RetGrounder improves grounding F1 to 33.9%, a 43% relative improvement. Our benchmark provides a reference point for measuring progress in the field of OCT diagnosis with MLLMs.

</details>

**extractive / en**

- 【課題】MLLMsが視覚的に網膜光コヒーレンストモグラフィー（OCT）、眼科で最も広く使用されている画像法で臨床所見を接地することができるかどうかは、主に未踏の
- 【方法】このギャップに対処するために、我々はRetinaGroundBench、網膜OCTのバイオマーカー視覚接地のための最初のベンチマークを導入します。
- 【従来からの進化】27のオープンソースMllm（0.8-38bパラメータ）にわたって、我々は視覚的な接地は、主に未解決のままであることがわかります：最高の汎用モデルは、バイオマーカーの存在

**q25-1.5b.gguf / en**（7.8 秒）

- 【課題】視覚的接地は、マルチモーダル大言語モデルを用いた網膜OCT診断では主に未解決のままである。
- 【方法】RetinaGroundBenchベンチマークとRetGrounder微調整されたモデル。
- 【従来からの進化】RetGrounderは視覚基づいているf1を33.9%、一般目的モデル上の43%の相対的な改善に改善する。

**q25-1.5b.gguf / ja**（6.4 秒）

- 【課題】临床问题的视觉定位
- 【方法】多模态大型语言模型（MLLM）
- 【従来からの進化】视觉定位仍不成熟

**q25-3b.gguf / en**（15.3 秒）

- 【課題】既存の作業は、MLLMsを用いた網膜OCTにおける視覚的接地のためのベンチマークを欠いている。
- 【方法】AggIoUメトリックとRetGrounderモデルとRetinaGroundBenchベンチマーク。
- 【従来からの進化】RetGrounderはf1の接地を23.7％から33.9％に改善します（43％の相対的な改善）。

**q25-3b.gguf / ja**（18.5 秒）

- 【課題】既存のMLLMsは医療画像の臨床的な質問に答える能力があるが、信頼性の高い使用には視覚的な地図が必要。Retinal OCTの視覚的な地図の地図化が不十分である。
- 【方法】RetinaGroundBenchを導入し、AggIoUを提案して視覚的な地図を評価。
- 【従来からの進化】RetGrounderを用いて視覚的な地図の精度を改善。

**q3-1.7b.gguf / en**（14.6 秒）

- 【課題】既存のMllmは、網膜OCTにおける視覚的接地と闘い、しばしば病変を部分的な予測に断片化する。
- 【方法】予測ボックスが注釈付き領域をカバーしているかどうかを評価するためにAggIoUを提案し、OCT特有のトレーニングを備えたRetGrounderを開発します。
- 【従来からの進化】RetGrounderは、より良いリコールと精度で、27MLLMs全体でf1の接地を33.9％（43％の改善）に改善します。

**q3-1.7b.gguf / ja**（12.8 秒）

- 【課題】既存手法では、Retinal OCTの病理を正確に識別できない
- 【方法】AggIoUを用いた視覚地図の評価とRetGrounderの開発
- 【従来からの進化】RetGrounderは43%の改善を達成し、OCT診断におけるMLLMの進展を示す

**q3-4b.gguf / en**（24.4 秒）

- 【課題】既存の研究では、マルチモーダル大言語モデルの網膜OCTにおける視覚的接地を評価するためのベンチマークが欠けています。
- 【方法】RetinaGroundBenchはAggIoUメトリックとRetGrounder、OCT固有の接地とテキストの統合のために微調整されたMLLMで、導入されています。
- 【従来からの進化】RetGrounderはf1の接地を33.9%に改善し、最高の汎用モデルよりも43%の相対的な改善をもたらします。

## 3. Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention

https://arxiv.org/abs/2610.31320

<details><summary>要旨（原文）</summary>

4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We adaptively aggregate these cues from multiple attention layers and across temporal windows, and fuse them with depth priors to handle challenging cases such as occlusions and textureless regions, producing precise dynamic masks that decouple static and dynamic regions. We then apply a soft key masking scheme that leverages these dynamic masks to suppress interference from dynamic regions in causal attention, thereby improving camera pose estimation accuracy. Stream4D inherits the efficiency of causal attention and remains compatible with existing streaming architectures. On diverse dynamic-scene benchmarks, Stream4D significantly improves camera pose estimation and static-scene reconstruction quality, yields reliable dynamic masks, and effectively mitigates long-sequence ghosting.

</details>

**extractive / en**

- 【課題】4Dシーンの再構成には、動的オブジェクトの堅牢な処理が必要ですが、既存のストリーミングメソッドは一般的に静的シーンを想定しており、長いシーケ
- 【方法】我々は、因果トランスバックボーン（例えば、StreamVGGT、Stream3R）に直接統合することができるトレーニングフリー、モーションデカップリングストリーミング再構成フレームワークStream4Dを
- 【従来からの進化】多様な動的シーンベンチマークでは、Stream4Dはカメラのポーズ推定と静的シーン再構成の品質を大幅に向上させ、信頼性の高い動的マスクを生成し、長いシーケンスゴースティングを効果的に軽減します。

**q25-1.5b.gguf / en**（6.9 秒）

- 【課題】4Dシーンの再構成には、動的オブジェクトの堅牢な処理が必要ですが、既存の方法では、ポーズドリフトやゴーストアーティファクトにつながる静的なシーンを想定しています。
- 【方法】Stream4dは、因果KVキャッシュアテンションを使用して静的領域と動的領域をデカップリングする、トレーニングフリーのモーションデカップリングストリーミング再構成フレームワークです。
- 【従来からの進化】Stream4dは、カメラの姿勢推定精度を向上させ、信頼性の高い動的マスクを生成し、長いシーケンスのゴーストを効果的に軽減します。

**q25-1.5b.gguf / ja**（6.7 秒）

- 【課題】4D scene reconstruction requires robust handling of dynamic objects, but existing methods assume static scenes, leading to pose drift and ghosting artifacts.
- 【方法】Stream4D is a training-free, motion-decoupled streaming reconstruction framework that decouples static and dynamic regions.
- 【従来からの進化】It uses causal KV-cache attention to implicitly encode rich temporal motion cues, improving accuracy and compatibility with existing architectures.

**q25-3b.gguf / en**（12.2 秒）

- 【課題】既存のストリーミング方法は、ダイナミックなシーンに苦労し、ポーズドリフトやゴーストアーティファクトにつながります。
- 【方法】因果KVキャッシュアテンションを使用したモーションデカップリングストリーミング再構成フレームワークであるStream4Dを紹介します。
- 【従来からの進化】カメラの姿勢推定と静的シーン再構成の品質を大幅に向上させ、長いシーケンスのゴーストを効果的に軽減します。

**q25-3b.gguf / ja**（23.0 秒）

- 【課題】動的なオブジェクトの処理が困難な4Dシーン再構築を処理する既存手法は、静的なシーンを仮定することが多い。これにより、長期間の序列でポーズのズレと幽霊化のアートifactsが発生する。
- 【方法】因果Transformerバックボーン（例：StreamVGGT、Stream3R）に直接統合可能な訓練不要のモーション脱却型ストリーミング再構築フレームワークStream4Dを提案。
- 【従来からの進化】因果注視がKVキャッシュに含まれる豊富な時系列のモーションの cuesを暗黙に含む。これらの cuesを複数の注視層と時間ウィンドウ間で適応的に集約し、深度のプライオリズムと融合することで、遮蔽やテキストレスの領域などの困難なケースを処理する。

**q3-1.7b.gguf / en**（10.2 秒）

- 【課題】既存のストリーミング方式では、静的なシーンを想定しており、長いシーケンスではポーズドリフトやゴーストが発生します。
- 【方法】Stream4dは因果KVキャッシュアテンションを使用して、時間的な動きの手がかりを適応的に集約し、深さのプライオリティと融合します。
- 【従来からの進化】Stream4Dはカメラの姿勢推定と静的シーン再構築を向上させ、15%+の精度向上と信頼性の高い動的マスクを実現します。

**q3-1.7b.gguf / ja**（15.0 秒）

- 【課題】既存手法では動的オブジェクトの処理が不十分で、長時間セリーブでは姿勢 driftと虚像が発生する
- 【方法】訓練不要で運動を分離した流動的な4D再構成フレームワークで、因果KVキャッシュアテンションを活用して時系列運動情報を抽出し、深さプライオリティを融合して動的マスクを生成する
- 【従来からの進化】効率的な因果アテンションを継承し、既存の流動的アーキテクチャと互換性があり、動的シーンでのカメラ姿勢推定と静的シーン再構成の精度を向上

**q3-4b.gguf / en**（19.1 秒）

- 【課題】既存のストリーミング方法は静的なシーンを想定しており、動的な4D再構成でポーズドリフトとゴーストを引き起こ
- 【方法】Stream4dは、トレーニングなしで運動と静的領域を分離し、時間的手がかりを適応させ、深度プライオリティと融合させるために因果KV-cache注意を使用しています。
- 【従来からの進化】Stream4dは、カメラのポーズ推定と静的再構成を改善し、信頼性の高い動的マスクを生成し、動的シーンベンチマークでのゴーストを軽減します。

## 4. AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation

https://arxiv.org/abs/2610.30097

<details><summary>要旨（原文）</summary>

Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies. However, existing VLA-RL methods typically suffer from delayed and biased credit assignment due to trajectory-level sparse rewards, while imbalanced subtask mastery creates bottlenecks that limit overall performance. To address these challenges, we propose AtomicRL, an RL post-training framework that leverages atomic task structures for reliable credit assignment and adaptive exploration. AtomicRL introduces Semantic-Aware Policy Optimization (SAPO), which uses semantic-aware gating to constrain TD residuals from failed atomic subtasks from propagating across task boundaries, mitigating credit contamination while preserving intra-subtask credit assignment and value bootstrapping. In addition, Bottleneck-Adaptive Target Exploration (BATE) dynamically coordinates task sampling and local exploration incentives based on the mastery of individual atomic subtasks, directing learning toward the remaining bottlenecks. Finally, we develop a Real2Sim2Real pipeline that bridges online RL in simulation with real-world deployment, facilitating practical transfer to physical robots. On LIBERO-LONG, AtomicRL achieves absolute performance gains of 3.6% and 4.0% over PPO across two VLA architectures. On CALVIN ABC-D, it improves full-task performance by up to 9.5% over PPO. Combined with the Real2Sim2Real pipeline, AtomicRL further improves real-world task performance by an average of 21.3%. These results demonstrate that AtomicRL effectively improves the learning efficiency and manipulation performance of VLA policies on long-horizon tasks.

</details>

**extractive / en**

- 【課題】しかし、既存のVLA-RLメソッドは、通常、軌道レベルのスパース報酬のために遅延および偏ったクレジット割り当てに苦しんでいますが、不均衡なサブタスクマスタリーは、全体的なパフォーマンスを制限するボトルネックを作成します。
- 【方法】これらの課題に対処するために、我々はAtomicRL、信頼性の高いクレジット割り当てと適応探査のための原子タスク構造を活用したRLポストトレーニングフレームワーク
- 【従来からの進化】LIBERO-LONGでは、AtomicRLは二つのVLAアーキテクチャにわたってPPOよりも3.6%と4.0%の絶対的なパフォーマンス向上を達成しています。

**q25-1.5b.gguf / en**（8.3 秒）

- 【課題】模倣学習は、視覚・言語・行動(VLA)モデルにおける複雑な長期的スキルの習得に苦労しています。
- 【方法】AtomicRLは、信頼性の高い与信割り当てと適応探査のために原子タスク構造を活用しています。
- 【従来からの進化】AtomicRLはPPOに比べて、それぞれLIBERO-LONGとCALVIN ABC-Dで3.6%、4.0%性能を向上させます。

**q25-1.5b.gguf / ja**（7.5 秒）

- 【課題】Imitation learning struggles with mastering complex long-horizon skills.
- 【方法】Reinforcement learning (RL) offers an effective avenue for improving VLA policies.
- 【従来からの進化】AtomicRL leverages atomic task structures for reliable credit assignment and adaptive exploration.

**q25-3b.gguf / en**（16.8 秒）

- 【課題】既存のVLA-RL法は、長期的なロボット操作タスクにおける遅延および偏ったクレジット割り当ておよび不均衡なサブタスク習得に苦労しています。
- 【方法】AtomicRLは、信頼性の高い与信割り当てと適応探査のために原子タスク構造を使用し、SAPOとBATEを導入します。
- 【従来からの進化】実世界のタスクパフォーマンスを最大21.3%向上させ、長期的なタスクのPPOを大幅に上回っています。

**q25-3b.gguf / ja**（18.0 秒）

- 【課題】VLAモデルがロボット操作で複雑な長期視野スキルを習得に苦戦する課題
- 【方法】AtomicRL: アトミックなタスク構造を用いた信用分配と探索の適応化
- 【従来からの進化】遅延と偏った信用分配、制約されたサブタスク masteryによるパフォーマンス制限の解消

**q3-1.7b.gguf / en**（14.1 秒）

- 【課題】既存のVLA-RL手法は、報酬の乏しさやサブタスクの習熟度のバランスの欠如により、クレジット割り当ての遅延やバイアスに悩まされています。
- 【方法】AtomicRLは、信頼性の高い与信割当のためのSAPOと、原子タスク構造を使用した適応探査のためのBATEを提案しています。
- 【従来からの進化】AtomicRLはLIBERO-LONGで3.6%と4.0%のパフォーマンス向上、CALVIN ABC-Dで9.5%、実際のタスクで21.3%のパフォーマンス向上を達成しています。

**q3-1.7b.gguf / ja**（14.3 秒）

- 【課題】既存手法では、長期的なロボット操作の学習に遅延や誤った信用分配が生じる
- 【方法】原子タスク構造を活用した信用分配と適応探索のためのSAPOとBATEを導入
- 【従来からの進化】3.6%～4.0%の性能向上、9.5%の全タスク性能向上、実世界での21.3%の改善

**q3-4b.gguf / en**（28.5 秒）

- 【課題】既存のVLA-RL法は、遅延および偏ったクレジット割り当てと、長い地平線のロボット操作における不均衡なサブタスクの習得に苦労しています。
- 【方法】AtomicRLは、単位の割り当てと探索に対処するためのsapoとBATEとのポストトレーニングフレームワークと、転送学習のためのReal2Sim2Realパイプラインを提案しています。
- 【従来からの進化】AtomicRLはLIBERO-LONGではPPOよりも3.6％と4.0％の改善を達成し、CALVIN ABC-Dでは9.5％の改善を達成し、21.3％の実世界のパフォーマンス向上を達成しています。

## 5. Bound-Conditioned Latent Inference for Progressive Image Compression

https://arxiv.org/abs/2610.30966

<details><summary>要旨（原文）</summary>

Progressive image compression reconstructs images from prefixes of a single bitstream and therefore involves sequential latent inference under partial observations. Existing trit-plane codecs mainly treat decoded trits as discrete symbols for probability prediction, without fully exploiting their role as interval constraints on the underlying continuous latents. We propose bound-conditioned latent inference (BLI), a framework that reformulates progressive trit-plane coding as sequential latent inference under shrinking interval constraints. At each coding step, the trits decoded so far define lower and upper bounds for each latent element. BLI uses the center and width of these bounds, together with hyperprior information shared by the encoder and decoder, to jointly refine the Gaussian parameters $(μ,σ)$ for entropy modeling and the latent estimate $\hat{y}$ for reconstruction. As additional trits are decoded, the feasible intervals shrink monotonically, yielding tighter constraints for the next inference step and enabling flexible in-plane refinement schedules. Experiments on Kodak, CLIC, and JPEG-AI show that BLI achieves state-of-the-art rate-distortion performance among progressive image codecs, reducing BD-rate by $17.78\%$ over DPICT and by $7.96\%$ over CTC on Kodak, while replacing CTC's plane-specific predictors with a shared model that uses about $5.3\times$ fewer parameters and achieves lower latency than CTC.

</details>

**extractive / en**

- 【課題】既存のｔｒｉｔ平面コーデックは，復号されたｔｒｉｔを確率予測のための離散シンボルとして扱うが，基礎となる連続ラテントに対する間隔制約としての役割を完全に利用することはない。
- 【方法】縮小区間制約の下で逐次潜在推論として漸進的ｔｒｉｔ平面符号化を再定式化する枠組みである束縛条件付き潜在推論（ＢＬＩ）を提案した。
- 【従来からの進化】実験のコダックCLICは、JPEG-AIることを示件を実現し最先端のレート歪みの性能の中で順送映像コーデック、BD削減-金$1,778発電電力量\%$過DPICTよ$7.96\%$過CTCにコダックを交換CTCの平面の特定のpredictors共有モデルを用いて$5.3\times$少ないパラメータを実現低遅延よりCTC.

**q25-1.5b.gguf / en**（8.2 秒）

- 【課題】プログレッシブ画像圧縮は、単一のビットストリームのプレフィックスから画像を再構成し、部分観測に基づく逐次潜在推論を含みます。
- 【方法】束縛条件付き潜在推論（ＢＬＩ）は，縮小区間制約の下で逐次潜在推論として漸進的ｔｒｉｔ平面符号化を再定式化した。
- 【従来からの進化】BLIは、境界の中心と幅をハイパープライオア情報とともに使用して、ガウスパラメータと潜在推定値を調整し、最先端のレート歪み性能を実現します。

**q25-1.5b.gguf / ja**（8.3 秒）

- 【課題】Progressive image compression reconstructs images from prefixes of a single bitstream, involving sequential latent inference under partial observations.
- 【方法】Proposed bound-conditioned latent inference (BLI) reformulates progressive trit-plane coding as sequential latent inference under shrinking interval constraints.
- 【従来からの進化】BLI uses bounds on latent elements to refine Gaussian parameters and latent estimates, enabling flexible in-plane refinement schedules and reducing BD-rate by 17.78% over DPICT and 7.96% over CTC.

**q25-3b.gguf / en**（17.0 秒）

- 【課題】既存のtrit-planeコーデックは、復号化されたtritを確率予測のための離散シンボルとして扱い、連続ラテンの区間制約としての役割を無視します。
- 【方法】縮小区間制約の下で逐次潜在推論として漸進的ｔｒｉｔ平面符号化を再定式化する束縛条件付き潜在推論（ＢＬＩ）を提案した。
- 【従来からの進化】最先端のレート歪み性能を実現し、BDレートをDPICTより17.78％、KodakのCTCより7.96％削減します。

**q25-3b.gguf / ja**（19.4 秒）

- 【課題】既存手法はデジタルビットストリームから画像を順次復元するプロ progressives画像圧縮で、部分的な観測下での順次潜在変数推論を扱う。
- 【方法】BLIは、縮小された区間制約下での順次潜在変数推論のフレームワークで、デジタルビットストリームから画像を順次復元するプロ progressives画像圧縮を提案する。
- 【従来からの進化】潜在変数の役割を完全に利用し、区間制約を縮小する順次潜在変数推論を行う。

**q3-1.7b.gguf / en**（13.3 秒）

- 【課題】既存のtrit-planeコーデックは、連続レイテンシ上の間隔制約としての役割を利用することなく、復号されたtritを離散シンボルとして扱います。
- 【方法】ＢＬＩは，境界の中心と幅とハイパープライオア情報を用いて，縮小区間制約の下で逐次潜在推論として漸進的ｔｒｉｔ平面符号化を再定式化した。
- 【従来からの進化】BLIはdpictより17.78%のBD率の減少およびCTCより7.96%の最新式の率ゆがみの性能、およびより低い潜伏の5.3倍のより少ない変数モデルを達成する。

**q3-1.7b.gguf / ja**（15.4 秒）

- 【課題】既存手法では、画像圧縮における部分観測下の連続ラテンツインフェンスが不十分で、効率的な圧縮が難しい。
- 【方法】境界条件付きラテンツインフェンス（BLI）を提案し、部分観測下のラテンツインフェンスを間隔制約で再構成する。
- 【従来からの進化】間隔制約を活用し、エントロピーモデリングとラテンツインフェンスのパラメータをより正確に推定し、効率的な圧縮を実現。

**q3-4b.gguf / en**（21.8 秒）

- 【課題】漸進的な画像圧縮は、部分的な観測の下で逐次潜在的推論を効率的に処理する上で限界に直面している。
- 【方法】縮小区間制約の下で逐次潜在推論として漸進的ｔｒｉｔ平面符号化を再定式化するための束縛条件付き潜在推論（ＢＬＩ）を提案した。
- 【従来からの進化】BLIは、最先端のレート歪み性能を実現し、BDレートをDpictより17.78%、KodakのCTCより7.96%削減します。

## 6. ResGVC: Residual Coding for High-fidelity Generative Video Compression

https://arxiv.org/abs/2610.31039

<details><summary>要旨（原文）</summary>

Generative video compression (GVC) methods usually employ decoder-side diffusion models to denoise reconstructed signals based on generative priors. Besides, most of these methods perform denoising in latent space rather than directly in pixel domain. In this paper, we propose ResGVC, a residual coding framework for GVC that guides denoising toward original pictures by transmitting residual signals. ResGVC first encodes the original pictures within a learned video codec, and then decomposes the distortion between the codec reconstruction and the original pictures into a sequence of residual segments, where each residual segment is acquired at each denoising step. Residual segments can further be compressed by a novel residual codec with a diffusion transformer as an entropy model. Unlike prior methods, ResGVC introduces explicit source constraints throughout denoising rather than relying on decoder-side generation alone. The diffusion-based entropy model also enables more effective distribution modeling capability based on the powerful generative priors. Moreover, denoising directly in pixel space avoids the irreversible information loss caused by latent representation bottlenecks. Experimental results show that, compared with the previous state-of-the-art method, ResGVC achieves 63.7% and 83.8% BD-rate reductions in terms of LPIPS and PSNR, respectively, while also delivering superior visual quality.

</details>

**extractive / en**

- 【課題】さらに、これらの方法のほとんどは、ピクセル領域で直接ではなく、潜在空間でノイズ除去を実行します。
- 【方法】本稿では，残留信号を送信することによって元の画像に向かってノイズ除去を導くｇｖｃの残留符号化フレームワークであるＲｅｓｇｖｃを提案した。
- 【従来からの進化】実験結果は、以前の最先端の方法と比較して、ResGVCは、優れた視覚品質を提供しながら、それぞれLPIPSとPSNRの面で63.7％と83.8％のBDレートの削減を達成することを示

**q25-1.5b.gguf / en**（8.4 秒）

- 【課題】生成ビデオ圧縮法は、多くの場合、復号器側の拡散モデルに依存して再構成された信号のノイズ除去を行い、ほとんどのノイズ除去はピクセル領域ではなく潜在的な空間で行われます。
- 【方法】ResGVCは、残差信号を送信することにより、元の画像に向かってノイズ除去をガイドする残差符号化フレームワークを提案しています。
- 【従来からの進化】ResGVCは、LPIPSおよびPSNRの点でそれぞれ63.7%および83.8%BD率の減少を達成し、また前の最新式の方法と比較される優秀な視覚質を提供している間。

**q25-1.5b.gguf / ja**（8.1 秒）

- 【課題】Generative video compression methods often use decoder-side diffusion models to denoise reconstructed signals based on generative priors, but most perform denoising in latent space rather than directly in pixel domain.
- 【方法】ResGVC is a residual coding framework for GVC that guides denoising toward original pictures by transmitting residual signals.
- 【従来からの進化】ResGVC introduces explicit source constraints throughout denoising rather than relying on decoder-side generation alone, enabling more effective distribution modeling based on powerful generative priors.

**q25-3b.gguf / en**（14.1 秒）

- 【課題】既存のGVC法は、潜在空間でのノイズ除去のためにデコーダ側拡散モデルに依存することがよくあります。
- 【方法】Ｒｅｓｇｖｃは，直接画素領域ノイズ除去のために歪みを残差セグメントに分解する残差符号化を提案している。
- 【従来からの進化】ResGVCは、優れた視覚品質で、LPIPSで63.7％のBDレート削減とPSNRで83.8％のBDレート削減を実現しています。

**q25-3b.gguf / ja**（18.0 秒）

- 【課題】GVCの既存手法は解像度の高い動画圧縮に課題を抱えている。
- 【方法】ResGVCは解像度の高い動画圧縮に向けたリマインダーコーディングフレームワークを提案。
- 【従来からの進化】解像度の高い動画圧縮に向けたリマインダーコーディングフレームワークを提案。

**q3-1.7b.gguf / en**（11.4 秒）

- 【課題】既存のGVCメソッドは潜在空間でノイズを除去し、不可逆的な情報損失をもたらします。
- 【方法】ResGVCは、ビデオコーデックで画像を符号化し、歪みを残差セグメントに分解し、拡散トランスで圧縮します。
- 【従来からの進化】ResGVCは、以前の方法と比較して、LPIPSで63.7％のBDレート削減とPSNRで83.8％を達成しています。

**q3-1.7b.gguf / ja**（14.5 秒）

- 【課題】既存手法では、画像の復元に依存し、圧縮効率が低く、視覚品質が劣る
- 【方法】残差信号を用いて、復元信号と原画像の差分を段階的に分解し、圧縮を実現する
- 【従来からの進化】明確なソース制約を導入し、潜在空間の損失を回避し、LPIPSとPSNRで63.7%～83.8%の改善を達成

**q3-4b.gguf / en**（22.4 秒）

- 【課題】既存のGVCメソッドは、ピクセル空間での効果的なノイズ除去を欠いており、限られた視覚品質での潜在的な空間ノイズ除去に依存しています。
- 【方法】Ｒｅｓｇｖｃは残差符号化フレームワークを用いて残差信号を送信することにより画素空間内のノイズを除去し，圧縮のエントロピーモデルとして拡散トランスを採用した。
- 【従来からの進化】ResGVCは、優れた視覚品質で、以前の最先端の方法と比較して、LPIPSとPSNRの63.7％と83.8％のBDレート削減を達成しています。

## 7. DRAFT: Decoding and Reconstructing 3D Room Layouts from fMRI and Camera Trajectories

https://arxiv.org/abs/2610.31108

<details><summary>要旨（原文）</summary>

While functional magnetic resonance imaging (fMRI) decoders reconstruct images and 3D objects, recovering the metric geometry of rooms from a moving viewpoint remains an open challenge. We introduce, to our knowledge for the first time, the task of reconstructing 3D layouts of held-out scenes using only the known camera trajectories and the fMRI signals of participants watching indoor walkthroughs, without any visual frames. The task is hard because of the temporal mismatch between rapid visual changes and blurred fMRI signals. Our method, DRAFT (Decoding and Reconstructing 3D room lAyouts from fMRI and Trajectories), extracts a compact layout representation from the early visual cortex and fuses this neural code with the geometric free space derived from camera motion. To evaluate it, we propose layout r, the Pearson correlation between predicted and ray-cast log depths. On ten held-out scenes (20 participants), DRAFT reaches a layout r of 0.480, outperforming the camera path alone (0.446) and seven fMRI decoders (at most 0.429). DRAFT also works as a plug-in that improves all seven decoders without retraining, raising their layout r from 0.171-0.429 to 0.487-0.493. Brain activity and camera motion can thus recover the metric layout of unseen rooms, a first step toward reconstructing the 3D spaces people see.

</details>

**extractive / en**

- 【課題】機能的磁気共鳴画像法(fMRI)デコーダーは画像や3D物体を再構築しますが、動く視点から部屋の計量幾何学を復元することは依然として未解決の課題です。
- 【方法】我々は、我々の知識に初めて、任意の視覚フレームなしで、屋内ウォークスルーを見て参加者の既知のカメラ軌跡とfMRI信号のみを使用して開催されたシーンの3Dレ
- 【従来からの進化】開催された10のシーン（20人の参加者）では、ドラフトは0.480のレイアウトrに達し、カメラパスのみ（0.446）および7つのfMRIデコーダ（最大0.429）を上回っています。

**q25-1.5b.gguf / en**（8.5 秒）

- 【課題】既知のカメラの軌跡とfMRI信号のみを使用して、保持されたシーンの3Dレイアウトを再構築する
- 【方法】ドラフト（fMRIと軌道からの3Dルームレイアウトのデコードと再構築）
- 【従来からの進化】0.480のレイアウトrに達し、カメラパスのみ（0.446）および7つのfMRIデコーダ（最大0.429）よりも優れています。

**q25-1.5b.gguf / ja**（6.9 秒）

- 【課題】recovering the metric geometry of rooms from a moving viewpoint
- 【方法】DRAFT (Decoding and Reconstructing 3D room layouts from fMRI and Trajectories)
- 【従来からの進化】improves fMRI decoders without retraining

**q25-3b.gguf / en**（16.1 秒）

- 【課題】既存の作業は、fMRI信号とカメラの軌跡から3Dルームレイアウトを再構築するのに苦労しています。
- 【方法】DRAFTは、初期の視覚野からコンパクトなレイアウト表現を抽出し、fMRI信号とカメラの軌道を使用して3D部屋のレイアウトをデコードし、再構築します。
- 【従来からの進化】DRAFTはホールドアウトシーンでレイアウトrを0.480と達成し、既存の手法を大幅に上回り、再訓練なしで7つのデコーダすべてを改善しています。

**q25-3b.gguf / ja**（14.9 秒）

- 【課題】fMRI信号とカメラの動径だけから3D室の配置を再構築する課題
- 【方法】DRAFT: fMRIとカメラの動径から3D室の配置を抽出・融合
- 【従来からの進化】従来の手法と比較して大幅に性能向上

**q3-1.7b.gguf / en**（14.0 秒）

- 【課題】Fmriとカメラの軌跡から3Dルームレイアウトを回復することは、視覚的変化とぼやけたfMRI信号との間の時間的不一致のために困難である。
- 【方法】DRAFTは、初期の視覚野からコンパクトなレイアウト表現を抽出し、カメラの動きから派生した幾何学的な自由空間と融合させます。
- 【従来からの進化】DRAFTは10シーンで0.480のレイアウトrを達成し、カメラパスと7つのfMRIデコーダを上回り、再トレーニングなしで7つのデコーダすべてを改善します。

**q3-1.7b.gguf / ja**（11.1 秒）

- 【課題】fMRI和相机轨迹重建3D房间布局存在时间不匹配问题
- 【方法】从fMRI和相机轨迹提取神经代码并融合几何空间
- 【従来からの進化】布局r达0.480，优于其他方法，可插件提升7个解码器

**q3-4b.gguf / en**（25.3 秒）

- 【課題】FMRIとカメラの軌跡から3Dルームメトリックジオメトリを再構築することは、時間的な不一致と視覚的なフレームの欠如のために困難なままです。
- 【方法】DRAFTは、初期の視覚野から得られたコンパクトなレイアウト表現と、カメラの動きから得られる幾何学的自由空間を融合させています。
- 【従来からの進化】ドラフトは、カメラパス（0.446）と七つのfMRIデコーダ（最大0.429）を上回って、十シーンで0.480のレイアウトrを達成します。

## 8. Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

https://arxiv.org/abs/2610.31166

<details><summary>要旨（原文）</summary>

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

</details>

**extractive / en**

- 【課題】動的シーンにおけるヒューマノイドロコ操作は非マルコフ的であり、オブジェクトが変化したり隠されたりすると手がかりは消えたり、ロボットが回転して歩いたりするとビューを離れたりしますが、全身視覚言語行動（VLA）ポリシーは現在のみを参照してください。
- 【方法】ロボットがその目標に作用する前に見られるオブジェクトイベントの前履歴を保持するオブジェクト誘導知覚メモリであるWholeBodyMemを提示します。
- 【従来からの進化】より多くのフレームではなく、適切なフレームを維持することで、WholeBodyMemは、シミュレーションで29.1％から72.6％に、実際のロボットで36.7％から88.3％に、標準的な単純なタスク（70.2％から86.9％）を改善しながら、メモリレスで統一されたメモリベースラインを上回っている。

**q25-1.5b.gguf / en**（6.7 秒）

- 【課題】動的なシーンでのヒューマノイドロコ操作は、手がかりとオブジェクトイベントの損失のために非マルコフです。
- 【方法】オブジェクト指向の知覚記憶であるWholeBodyMemは、オブジェクトイベントの前の履歴を保持します。
- 【従来からの進化】WholeBodyMemは、シミュレーションや実際のロボットでの成功率を向上させ、メモリレスと一様メモリベースラインを上回ります。

**q25-1.5b.gguf / ja**（7.1 秒）

- 【課題】Humanoid loco-manipulation in dynamic scenes is non-Markovian due to object events changing or being hidden.
- 【方法】WholeBodyMem, an object-guided perceptual memory, keeps the pre-history of object events.
- 【従来からの進化】WholeBodyMem surpasses memoryless and uniform-memory baselines in simulation and real robot tasks.

**q25-3b.gguf / en**（14.8 秒）

- 【課題】既存の作品は、オブジェクトが変化したり隠されたりするにつれて手がかりが消えるヒューマノイドロコ操作の非マルコフシーンと格闘しています。
- 【方法】オブジェクト指向のプリヒストリーメモリを使用してキーフレームを保持し、ポリシーの成功率を向上させます。
- 【従来からの進化】WholeBodyMemは、シミュレーションで29.1％から72.6％に、実際のロボットで36.7％から88.3％に成功率を上げ、メモリレスと均一メモリベースラインを上回ります。

**q25-3b.gguf / ja**（13.3 秒）

- 【課題】非マーカルの状況でロボットが目標を達成するための非一貫性を克服する課題
- 【方法】WholeBodyMem: 事前歴の物体イベントを記憶する物体指向の感知記憶
- 【従来からの進化】記憶したフレームの選択により、基準の成功率を大幅に向上

**q3-1.7b.gguf / en**（12.7 秒）

- 【課題】動的なシーンでのヒューマノイドロコ操作は非マルコビアンであり、オブジェクトが変化したり隠されたりすると手がかりは消えます。
- 【方法】WholeBodyMemは、オブジェクト指向の知覚メモリを使用して、目標に作用する前にオブジェクトイベントの事前履歴を保持します。
- 【従来からの進化】WholeBodyMemは、シミュレーションで29.1％から72.6％に、実際のロボットで36.7％から88.3％に成功率を向上させ、メモリレスおよび一様メモリベースラインを上回っています。

**q3-1.7b.gguf / ja**（9.7 秒）

- 【課題】既存手法では、動的シーンでのロボットの動作に伴う情報消失が問題
- 【方法】オブジェクトガイドされた視覚記憶を用い、過去のイベントを保持する
- 【従来からの進化】フレーム数を適切に制限し、成功率を向上

**q3-4b.gguf / en**（23.6 秒）

- 【課題】ダイナミックなシーンは、現在の政策を現在のみに制限し、手がかりの消失と視点の変更によるヒューマノイドのロコ操作に挑戦します。
- 【方法】WholeBodyMemは、オブジェクト-ガイド付きメモリを使用して、オブジェクト-イベントの事前履歴を保持し、因果追跡とオブジェクト-トークンとの交差注意を介してキー-フレームを選択します。
- 【従来からの進化】WholeBodyMemは、シミュレーションで29.1％から72.6％、実際のロボットで36.7％から88.3％に成功率を向上させ、標準タスクも70.2％から86.9％に向上させます。

## 9. Moving Regions, Not Moving Objects: Segmenting What Actually Moves under Camera Motion

https://arxiv.org/abs/2610.31209

<details><summary>要旨（原文）</summary>

Moving object segmentation is conventionally formulated at the sequence and object level, marking an entire instance as moving once it moves anywhere in a video. Recent instantaneous formulations distinguish moving from stationary intervals, but still generate masks at the object level through frozen segmentation foundation models. Because the mask is derived from an instance-level proposal, motion is typically attributed to the entire instance rather than localized to the regions that actually move. Moreover, such instance-level predictions can produce masks even when no part of the instance is actually moving, revealing a more fundamental issue: motion is not an intrinsic property of an instance; it can only be determined by comparing at least two frames. Building on this premise, we introduce MoRSe, which jointly interprets two frames to predict a moving-region mask, distinguishing actual scene motion from apparent motion induced by the camera. A single RGB encoder replaces multi-stage foundation stacks, so no optical flow, point tracks, or separate mask generator is needed at inference. We release MoRSe-5K, a benchmark of 42 sequences with Static, Dynamic-Static, and Dynamic settings designed to evaluate the model's ability to distinguish and localize moving and stationary regions under different camera and scene motion conditions. MoRSe outperforms both specialized moving object segmentation methods and dense 4D reconstruction methods with motion-thresholded predictions, while producing the fewest false positives on sequences where nothing moves.

</details>

**extractive / en**

- 【課題】さらに、このようなインスタンスレベルの予測は、インスタンスの全てが動いていなくてもマスクを生成することがあり、より根本的な問題が明らかになります。すなわち、動きはインスタンスの本質的な性質ではないということです。少なくとも2つのフレームを比較することでのみ判定できます。
- 【方法】この前提に基づいて，二つのフレームを共同で解釈して移動領域マスクを予測するモールスを導入し，実際のシーンの動きとカメラによって誘導される見かけの動きを区別した。
- 【従来からの進化】モールスは、何も動かないシーケンスで最も少ない偽陽性を生成しながら、動きしきい値予測と特殊な移動物体セグメンテーション法と密な4D再構成法の両方

**q25-1.5b.gguf / en**（8.7 秒）

- 【課題】移動オブジェクトのセグメンテーションは、通常、シーケンスとオブジェクトレベルで定式化され、ビデオ内の任意の場所を移動すると、インスタンス全体が移動したものとしてマークされます。
- 【方法】二つのフレームを共同で解釈して移動領域マスクを予測し，実際のシーンの動きとカメラによって誘導される見かけの動きを区別した。
- 【従来からの進化】モールスは、何も動かないシーケンスで最も少ない偽陽性を生成しながら、動きしきい値予測と特殊な移動物体セグメンテーション法と密な4D再構成法

**q25-1.5b.gguf / ja**（7.0 秒）

- 【課題】Moving object segmentation is conventionally formulated at the sequence and object level, marking an entire instance as moving once it moves anywhere in a video.
- 【方法】Jointly interpreting two frames to predict a moving-region mask.
- 【従来からの進化】Improves the ability to distinguish and localize moving and stationary regions under different camera and scene motion conditions.

**q25-3b.gguf / en**（14.4 秒）

- 【課題】既存の作業は、実際の移動領域を区別するために失敗し、移動としてオブジェクト全体をセグメン
- 【方法】モールスは、カメラによる動きと区別して、移動領域を予測するために二つのフレームを共同で解釈します。
- 【従来からの進化】モールスは、偽陽性の少ない特殊な方法よりも優れており、最先端のパフォーマンスを実現しています。

**q25-3b.gguf / ja**（16.2 秒）

- 【課題】既存手法は全体のオブジェクトを動くとみなすため、動く部分が特定されず、カメラの動かしによる誤った動きも検出される問題
- 【方法】MoRSeは2フレームを同時に解釈し、実際に動く部分を動く領域として予測する
- 【従来からの進化】インスタンスレベルの予測から解放され、静止部分も正確に識別できる

**q3-1.7b.gguf / en**（11.2 秒）

- 【課題】既存のメソッドでは、パーツのみが移動するとインスタンス全体が移動するようにセグメント化され、モーションアトリビューションが不正確になります。
- 【方法】モールスは、2つのフレームを共同で解釈して移動領域マスクを予測し、インスタンスレベルの予測を回避します。
- 【従来からの進化】モールスは、実際の動きと見かけの動きを区別するためのより高い精度を達成し、動かないシーケンスでの偽陽性が1.2％少なくなります。

**q3-1.7b.gguf / ja**（12.4 秒）

- 【課題】既存手法では、動く物体を正確に分割できない
- 【方法】2フレームを同時に解釈し、実際の動きを区別する移動領域マスクを予測
- 【従来からの進化】単一のRGBエンコーダーでマルチステージの基礎モデルを置き換えることで、光学流や点追跡を必要とせず、少ない誤り率で高い精度を達成

**q3-4b.gguf / en**（20.9 秒）

- 【課題】既存の手法では、動きを局所的な移動領域ではなくインスタンス全体に帰属させています。
- 【方法】Ｍｏｒｓｅは二つのフレームを共同で解釈し，光学流または別個のマスクジェネレータなしで移動領域マスクを予測した。
- 【従来からの進化】モールスは精度において他の方法よりも優れており、特に動きのないシーケンスでは偽陽性が少なくなります。

## 10. Self-Distilling Future Video Representations for World Action Models

https://arxiv.org/abs/2610.30320

<details><summary>要旨（原文）</summary>

World Action Models (WAMs) have emerged as a promising approach to learning generalist robot policies using rich spatiotemporal priors from pre-trained video diffusion models. A recent line of WAMs improves inference efficiency by conditioning a separate action decoder on intermediate future video representations extracted from a single denoising step, avoiding costly iterative denoising required for video generation. This design makes action prediction depend directly on the quality of these future representations. In this paper, we introduce Future REpresentation learning via self-Distillation with temporal context (FRED), a framework that trains WAMs to improve the quality of future video representations from noise in a single denoising step. Specifically, FRED uses self-distillation to predict future representations from noise, using representations extracted from ground-truth future observations as targets. We further condition the video model on historical observations, providing temporal context for predicting future representations better. Across diverse real-world manipulation scenarios, FRED consistently outperforms competing WAMs. It achieves particularly large gains on long-horizon and out-of-domain tasks under zero-shot environment generalization, and substantially improves human-to-robot skill transfer, reaching 50.0% task success on tasks absent from robot training data and demonstrated only in human videos, compared with 19.4% for the best competing WAM.

</details>

**extractive / en**

- 【課題】最近の一連のWAMsは、単一のノイズ除去ステップから抽出された中間の将来のビデオ表現に別々のアクションデコーダを調整することにより、推論効率を
- 【方法】本稿では，単一のノイズ除去ステップでノイズから将来のビデオ表現の品質を向上させるためにＷａｍを訓練するフレームワークである時間的文脈（ＦＲＥＤ）を用いた自己蒸留による将来の表現学習を導入した。
- 【従来からの進化】これは、ゼロショット環境の一般化の下で、長い地平線とドメイン外のタスクで特に大きな利益を達成し、大幅にロボットへのスキル転送を改善し、ロ

**q25-1.5b.gguf / en**（8.5 秒）

- 【課題】推論の効率と一般化を強化するために、World Action Models（Wam）の将来のビデオ表現の品質を向上させる。
- 【方法】FRED(future REpresentation learning via self-Distillation with temporal context)は、地上真実の将来の観測を使用してノイズから将来の表現を予測するためにWAMsを訓練します。
- 【従来からの進化】FREDは、さまざまな現実世界の操作シナリオで競合するWamを一貫して上回り、ゼロショット環境の一般化の下で長い地平線とドメイン外のタスクで大

**q25-1.5b.gguf / ja**（7.7 秒）

- 【課題】Existing methods for inference efficiency in WAMs require costly iterative denoising for video generation.
- 【方法】FRED (Future Representation learning via self-Distillation with temporal context) trains WAMs to improve future video representation quality from noise in a single denoising step.
- 【従来からの進化】FRED uses self-distillation to predict future representations from noise, using ground-truth future observations as targets, and provides temporal context for better prediction.

**q25-3b.gguf / en**（12.9 秒）

- 【課題】WAMsにおける将来のビデオ表現の推論効率と品質を向上させます。
- 【方法】ノイズからの将来のビデオ表現を改善するために、時間的文脈を用いた自己蒸留。
- 【従来からの進化】人間からロボットへのスキル転送を大幅に改善し、目に見えないタスクで50.0％のタスク成功を達成します。

**q25-3b.gguf / ja**（14.5 秒）

- 【課題】WAMsの予測精度が課題
- 【方法】FRED:未来視覚表現の質を改善する自ディストリビューション学習
- 【従来からの進化】単一の去ノイズステップで未来視覚表現の品質を向上

**q3-1.7b.gguf / en**（12.0 秒）

- 【課題】既存のWamは、将来のビデオ表現のためにコストのかかる反復ノイズ除去に依存しており、アクション予測を品質に敏感にします。
- 【方法】FREDは、地上観測からの自己蒸留と時間的文脈を使用して、ノイズから将来のビデオ表現を予測するためにWAMsを訓練します。
- 【従来からの進化】FREDは、ドメイン外のタスクで50.0%のタスク成功を達成し、長期的なタスクで30.6%の以前の作業を上回っています。

**q3-1.7b.gguf / ja**（13.3 秒）

- 【課題】既存手法では未来ビデオ表現の質が低下し、効率的な動作モデルの学習に課題がある。
- 【方法】FREDは自適応蒸馏を用いて、単一のノイズステップから未来ビデオ表現を学習する。
- 【従来からの進化】零-shot環境一般化において長時間 horizonと出域タスクに大きな改善、人間とロボットのスキル転移に顕著な効果。

**q3-4b.gguf / en**（22.5 秒）

- 【課題】既存のWAMは将来の映像表現のために高コストな反復ノイズ除去に依存しており、推論効率を制限しています。
- 【方法】FREDは自己蒸留を使用して、過去の観測からの時間的文脈を用いて、単一のノイズ除去ステップでノイズからの将来のビデオ表現を改善するためにWAMs
- 【従来からの進化】FREDはドメイン外タスクで50.0%のタスク成功率を達成し、競合するWAMでは19.4%にとどまり、ゼロショットの一般化とスキル移転を向上させています。

## 11. One-shot federated unsupervised domain adaptation with Smoothed Knowledge Distillation and teacher refinement

https://arxiv.org/abs/2610.30646

<details><summary>要旨（原文）</summary>

Federated unsupervised domain adaptation (FUDA) addresses the challenge of adapting models to an unlabeled target domain using decentralized source domains while preserving data privacy. However, existing FUDA methods typically require multiple communication rounds, rely on complex aggregation strategies, and often struggle with noisy pseudo labels and inconsistent source knowledge. To address these challenges, we propose SKD-ETR, a novel one-shot FUDA framework that combines Smoothed Knowledge Distillation (SKD) and Exponential moving average-based Teacher Refinement (ETR). SKD trains a student model on the target domain using smoothed soft pseudo labels generated by the ensemble of source models. This reduces overconfidence, mitigates noise, and improves robustness. ETR further refines each source model by interpolating its parameters toward the student via exponential moving average (EMA), thereby transferring target-domain knowledge back to the teachers. This bidirectional refinement enhances pseudo-label quality and student generalization without additional communication overhead. SKD-ETR eliminates complex aggregation by initializing the student model randomly and performing a single-round distillation process. Extensive experiments on OfficeHome, Office-Caltech, and DomainNet demonstrate that SKD-ETR achieves competitive performance while being communication- and computation-efficient, and robust under noisy supervision. The code for this paper is available at https://github.com/A-Abedi/SKD_ETR.

</details>

**extractive / en**

- 【課題】しかし、既存のFUDAメソッドは、通常、複数の通信ラウンドを必要とし、複雑な集約戦略に依存し、多くの場合、ノイズの多い擬似ラベルと一貫性のないソース
- 【方法】これらの課題に対処するため、私たちはスムークスド・ナレッジ・ディスティレーション(SKD)と指数移動平均ベースの教師精錬(ETR)を組み合わせた新しいワンショットFUDAフレームワークSKD-ETRを提案します。
- 【従来からの進化】これにより、過信が軽減され、ノイズが軽減され、堅牢性が向上します。

**q25-1.5b.gguf / en**（8.9 秒）

- 【課題】フェデレーションされた教師なしドメイン適応（FUDA）は、複数の通信ラウンドと複雑な集約戦略を必要とし、ノイズの多い擬似ラベルと一貫性のないソー
- 【方法】SKD-ETRは、平滑化された知識蒸留（SKD）と指数移動平均ベースの教師洗練（ETR）を組み合わせて、ソースモデルのアンサンブルによって生成された平滑化されたソフト擬似ラベルを使用して、ターゲットドメイン上の学生モデルを訓練する。
- 【従来からの進化】SKD-ETRは、学生モデルをランダムに初期化し、単一ラウンド蒸留プロセスを実行することにより、複雑な集約を排除し、通信と計算の効率を高めながら競争力のあるパフォーマンスを実現します。

**q25-1.5b.gguf / ja**（7.1 秒）

- 【課題】Adapting models to an unlabeled target domain using decentralized source domains while preserving data privacy
- 【方法】Combining Smoothed Knowledge Distillation (SKD) and Exponential moving average-based Teacher Refinement (ETR)
- 【従来からの進化】One-shot FUDA framework that reduces overconfidence, mitigates noise, and improves robustness

**q25-3b.gguf / en**（14.1 秒）

- 【課題】既存のFUDAメソッドは、通信の複数のラウンドを必要とし、ノイズの多い擬似ラベルとの闘争。
- 【方法】SKD-ETRは、SKDとETRを組み合わせて、平滑化された擬似ラベルを使用してターゲットドメイン上の学生モデルを訓練し、EMAを介してソースモデルを精緻化します。
- 【従来からの進化】SKD-ETRは、ワンショットトレーニングで競争力のあるパフォーマンスを実現し、通信と計算のオーバーヘッドを削減します。

**q25-3b.gguf / ja**（13.9 秒）

- 【課題】複数の通信ラウンドと複雑な aggregation 策略による課題
- 【方法】SKD-ETR: SKDとETRの組み合わせによる1ラウンドFUDA
- 【従来からの進化】シンプルな初始化と1ラウンドの知識伝送

**q3-1.7b.gguf / en**（14.0 秒）

- 【課題】既存のFUDAメソッドは、複数の通信ラウンドを必要とし、複雑な集約戦略に依存し、ノイズの多い擬似ラベルと一貫性のないソース知識に苦労します。
- 【方法】SKD-ETRは、平滑化された知識蒸留（SKD）と指数移動平均ベースの教師洗練（ETR）を組み合わせて、平滑化された擬似ラベルを使用してターゲットドメイン上の学生モデ
- 【従来からの進化】SKD-ETRは、通信と計算の効率的なトレーニングにより、OfficeHome、Office-Caltech、DomainNetで競争力のあるパフォーマンスを実現し、追加の通信オーバーヘッドなしで擬似ラベルの品質と学生

**q3-1.7b.gguf / ja**（11.6 秒）

- 【課題】既存FUDA方法の複数回通信、ノイズ対処の困難
- 【方法】SKDとETRを組み合わせた1回通信のFUDAフレームワーク
- 【従来からの進化】過信を減らし、ノイズを軽減し、効率的な知識伝達

**q3-4b.gguf / en**（22.4 秒）

- 【課題】既存のFUDAメソッドは、ノイズの多い擬似ラベル、一貫性のないソース知識に苦労し、複数の通信ラウンドを必要とします。
- 【方法】SKD-ETRは、平滑化された知識蒸留と指数移動平均ベースの教師の洗練を組み合わせて、双方向の洗練とワンショットFUDAを達成します。
- 【従来からの進化】SKD-ETRは、OfficeHome、Office-Caltech、DomainNet上でノイズの多い監督下でも通信および計算効率、堅牢性で競争力を発揮します。

## 12. Evidence-Guided Selection of Retinal Vessel Segmentation Pipelines: A Cross-Dataset Benchmark of Performance, Structure, Failure Modes, and Reproducibility

https://arxiv.org/abs/2610.35357

<details><summary>要旨（原文）</summary>

Retinal vessel segmentation is widely used in retinal image analysis, yet model selection based only on aggregate overlap scores can overlook structural fidelity, cross-dataset robustness, and application-specific error costs. We evaluated five executable binary vessel-segmentation pipelines (FSG-Net, SA-UNetv2, DCP-1024, GAVE, and FR-UNet) on 244 images from six public datasets using pixel-level agreement, cross-dataset stability, thin-vessel retention, structural metrics, error composition, and available computational evidence. Results were aggregated with equal weighting across datasets. No pipeline was optimal in every setting. FSG-Net achieved the highest equal-dataset mean Macro-F1 (0.77), IoU (0.63), clDice (0.83), and Skeleton F1 (0.78), whereas SA-UNetv2 achieved the highest mean sensitivity (0.85) and Thin-Vessel Sensitivity (0.63). Differences across datasets were often larger than those among the leading pipelines, and errors shared by all five methods were concentrated near annotated vessel boundaries and faint peripheral vessels. In an ancillary analysis on 45 HRF images, segmentation masks were converted into 11 ring-wise vascular features for leave-one-out classification. Controlled perturbations showed that local mask errors can be amplified in downstream features, while targeted stabilization reduced sensitivity for five features. The results support task-conditioned, benchmark-relative pipeline selection rather than a single universal ranking and highlight the need to validate the selected pipeline on the intended target domain.

</details>

**extractive / en**

- 【課題】（空欄）
- 【方法】（空欄）
- 【従来からの進化】（空欄）

**q25-1.5b.gguf / en**（13.2 秒）

- 【課題】集計オーバーラップスコアに基づくモデル選択は、構造の忠実度、クロスデータセットの堅牢性、およびアプリケーション固有のエラーコストを見落とす可能性があります。
- 【方法】我々は、ピクセルレベルの合意、クロスデータセットの安定性、薄容器保持、構造メトリック、誤差組成、および利用可能な計算証拠を使用して六つの公共データセットから244画像上の五つの実行可能なバイナリ容器セグメンテーションパイプライン（FSG-Net、SA-Unetv2、DCP-1024、GAVE、およびFR-UNet）を評価した。
- 【従来からの進化】FSG-Netは、最高の等しいデータセットの平均マクロF1（0.77）、IoU（0.63）、clDice（0.83）、およびスケルトンF1（0.78）を達成したが、SA-Unetv2は最高の平均感度（0.85）と薄容器感度（0.63）を達成した。 データセット間の差は、主要なパイプライン間の差よりもしばしば大きく、五つの方法すべてで共有される誤差は、注釈付きの血管境界およびかすかな周辺血管の近くに集中していた。

**q25-1.5b.gguf / ja**（17.1 秒）

- 【課題】模型选择基于仅基于聚合重叠分数的模型选择忽略结构忠实度、跨数据集稳健性和应用特定错误成本。
- 【方法】评估五种可执行的二元血管分割管道（FSG-Net、SA-UNetv2、DCP-1024、GAVE、FR-UNet）在六个公共数据集上的244张图像，使用像素级一致性、跨数据集稳定性、细血管保留、结构指标、错误组成和可用计算证据。
- 【従来からの進化】结果被加权平均，没有管道在所有设置中都是最优的。FSG-Net在每个数据集上的平均Macro-F1（0.77）、IoU（0.63）、clDice（0.83）和Skeleton F1（0.78）最高，而SA-UNetv2在平均敏感性（0.85）和细血管敏感性（0.63）上最高。不同数据集之间的差异往往大于领先管道之间的差异，所有五种方法的错误都集中在标注血管边界和微弱的外围血管附近。在45张HRF图像上，将分割掩码转换为11个环状血管特征，进行留一分类。控制扰动显示局部掩码错误在下游特征中可以放大，而靶向稳定减少了五个特征的敏感性。结果支持任务条件化的基准相对管道选择，而不是单个通用排名，强调了选择的管道在预期目标域上验证的需要。

**q25-3b.gguf / en**（16.1 秒）

- 【課題】既存の作業では、モデルの選択における構造の忠実度、クロスデータセットの堅牢性、およびアプリケーション固有のエラーコストが見過ごされています。
- 【方法】複数のメトリクスとエラーモードを使用して六つのデータセット上の五つの網膜血管セグメンテーションパイプラインを評価した。
- 【従来からの進化】FSG-NetとSA-Unetv2は、さまざまな設定で最適であり、タスク条件付きパイプラインの選択の必要性を強調しています。

**q25-3b.gguf / ja**（21.3 秒）

- 【課題】aggregate overlap scoresの限界で、構造的信頼性や跨データセットの堅牢性、アプリケーション固有のエラーコストを無視している。
- 【方法】5つの実行可能な二値血管分割パイプラインを6つの公開データセットから評価し、ピクセルレベルの合致、跨データセットの安定性、細血管の保持、構造指標、エラー構成、可用なコンピュータービジネスを用いた。
- 【従来からの進化】跨データセットの安定性と構造指標の評価により、選択したパイプラインの性能を改善。

**q3-1.7b.gguf / en**（14.7 秒）

- 【課題】既存の方法では、構造の忠実度、クロスデータセットの堅牢性、および船舶のセグメンテーションにおけるアプリケーション固有のエラーコストを説明できません。
- 【方法】ピクセルレベルの一致、安定性、およびエラー解析を使用して、複数のデータセット上の五つのセグメンテーションパイプラインを評価します。
- 【従来からの進化】FSG-NetはMacro-F1、IoU、clDice、Skeleton F1で他のものよりも優れています。SA-Unetv2は感度と薄容器感度に優れています。

**q3-1.7b.gguf / ja**（14.1 秒）

- 【課題】既存手法が構造的信頼性や適用特定の誤りコストを考慮していない
- 【方法】5つのバイナリパイプラインを多データセットで評価し、性能、構造、エラーコンポジションを分析
- 【従来からの進化】FSG-Netが最も高かったが、他のパイプラインも優れた結果を示し、単一の普遍的なランキングは不適

**q3-4b.gguf / en**（30.1 秒）

- 【課題】網膜血管セグメンテーションのための既存のモデル選択は、集約メトリック、構造忠実度の欠如、およびクロスデータセットの堅牢性に依存しています。
- 【方法】この論文では、パフォーマンス、安定性、エラータイプ、再現性を分析し、六つのデータセットにわたって244の画像上の五つのセグメンテーショ
- 【従来からの進化】FSG-Netは最高のマクロF1（0.77）、IoU（0.63）、clDice（0.83）、スケルトンF1（0.78）を達成し、SA-Unetv2は最高の感度（0.85）と薄容器感度（0.63）を持っていました。

## 13. KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling

https://arxiv.org/abs/2610.30609

<details><summary>要旨（原文）</summary>

Unmanned aerial vehicles (UAVs) have recently emerged as important remote sensing platforms, and UAV navigation has shown great potential in remote sensing applications. However, existing methods do not explicitly incorporate kinodynamic modeling or safety distances into trajectory generation, resulting in high absolute yaw rates, frequent collisions, and low navigation success rates, which limit safety and motion stability. To address this challenge, we introduce KinoUAV, a kinodynamic benchmark comprising a dataset and KinoUAV-Agent. First, we develop a hierarchical kinodynamic trajectory generation pipeline that drives UAV through acceleration actions. It uses waypoint chains from global planning and generates trajectories segment by segment under velocity, acceleration, and jerk constraints, reducing oscillations and improving trajectory stability. Furthermore, we introduce directional free-space distance (DFD) labels into the constructed dataset to describe the available clearance for safe motion decisions. The proposed KinoUAV-Agent predicts DFDs and uses them to generate safe actions, decoupling perception from action decision-making. This design enables autonomous obstacle avoidance and improves navigation safety. The benchmark incorporates the proposed Cruise-Seek task, in which the UAV first enters the target region and then searches for the target, reducing the difficulty of target search and improving navigation success. Experiments on KinoUAV show that KinoUAV-Agent outperforms existing methods, achieving the highest success rate while maintaining lower absolute yaw rates and collision rates. These results demonstrate the effectiveness of kinodynamic modeling for safe and stable UAV navigation.

</details>

**extractive / en**

- 【課題】しかし、既存の方法では、運動力学的モデリングや安全距離を軌道生成に明示的に組み込んでいないため、高い絶対ヨー率、頻繁な衝突、および低い航法成功率が生じ、安全性と運動安定性が制限されます。
- 【方法】この課題に対応するため、データセットとKinoUAV-AgentからなるキノダイナミックベンチマークであるKinoUAVを導入します。
- 【従来からの進化】それは全体的な計画からのウェイポイントの鎖を使用し、振動を減らし、弾道の安定性を改善する速度、加速およびジャークの抑制の下で区分ごとに軌道を発生させる。

**q25-1.5b.gguf / en**（9.9 秒）

- 【課題】既存の手法では、運動動力学モデリングや安全距離を軌道生成に明示的に組み込んでおらず、そのため絶対ヨー率が高く、衝突が頻繁になり、航法成功率も低くなります。
- 【方法】データセットとＫｉｎｏｕａｖ-Ａｇｅｎｔからなるｋｉｎｏｕａｖを紹介した。 パイプラインは、グローバルな計画からウェイポイントチェーンを使用して、振動を低減し、軌道の安定性を向上させ、速度、加速度、およびジャーク制約の下でセグ 安全な運動決定のための利用可能なクリアランスを記述するために方向自由空間距離（ＤＦＤ）ラベルを導入した。
- 【従来からの進化】ベンチマークには提案された巡航・探索タスクが組み込まれており、航行安全性の向上と目標探索の難易度の軽減が図られています。

**q25-1.5b.gguf / ja**（7.9 秒）

- 【課題】Existing methods do not incorporate kinodynamic modeling or safety distances into trajectory generation, leading to high absolute yaw rates, frequent collisions, and low navigation success rates.
- 【方法】Introduce KinoUAV, a kinodynamic benchmark with a hierarchical trajectory generation pipeline and directional free-space distance labels.
- 【従来からの進化】KinoUAV-Agent decouples perception from action decision-making, enabling autonomous obstacle avoidance and improved navigation safety.

**q25-3b.gguf / en**（15.9 秒）

- 【課題】既存の方法では、運動力学的モデリングと安全距離が不足しているため、高いヨー率、頻繁な衝突、および低い成功率につながります。
- 【方法】階層的な軌道生成と方向自由空間距離ラベルを持つkinouav、kinodynamicベンチマークを紹介します。
- 【従来からの進化】より低いヨー率および衝突率を維持している間最も高い成功率（90%）を達成する。

**q25-3b.gguf / ja**（17.7 秒）

- 【課題】既存手法は安全距離やダイナミックモデルを含まないため、高 yaw レート、頻繁な衝突、低 Navigation 成功率が問題
- 【方法】ダイナミックモデルを含む階層的なダイナミックトラジェクトリーゲネレーティングパイプラインを導入
- 【従来からの進化】安全な行動を生成するための感知と行動決定の分離により、自動的な障害物回避と Navigation 安全性の改善

**q3-1.7b.gguf / en**（11.8 秒）

- 【課題】既存の方法では、運動力学的モデリングと安全距離が不足しているため、高いヨー率、衝突、および低いナビゲーションの成功につながります。
- 【方法】KinoUAVは安全な弾道の生成および障害回避のための階層的なkinodynamicパイプラインそしてDFDのラベルを導入する。
- 【従来からの進化】KinoUAV-Agentは、従来の作業と比較してヨー率や衝突率が低くなり、最高のナビゲーション成功率を達成しています。

**q3-1.7b.gguf / ja**（14.3 秒）

- 【課題】既存手法では、運動制約や安全距離を明確に考慮していないため、振動や衝突が発生し、ナビゲーション成功率が低く
- 【方法】階層的な運動制御トラッキングパイプラインと方向性自由空間距離（DFD）ラベルの導入により、安全な動作生成を実現
- 【従来からの進化】ナビゲーション成功率が最高に達し、振動と衝突率が低く、運動制御の安定性が向上

**q3-4b.gguf / en**（21.2 秒）

- 【課題】既存の方法は、kinodynamicモデリングと安全距離を欠いており、危険で不安定なUAVナビゲーションにつながります。
- 【方法】KinoUAVは安全な動きの決定のための弾道の生成のパイプラインそしてDFDのラベルが付いているkinodynamic基準を導入する。
- 【従来からの進化】KinoUAV-Agentはヨー率や衝突率を低くし、高い成功率を達成し、安全性と安定性の向上を示しています。

## 14. DRILL: Training World Models to Improve Policies, Not Predict Pixels

https://arxiv.org/abs/2610.30814

<details><summary>要旨（原文）</summary>

World models are increasingly used to reduce environment interaction when post-training vision-language-action (VLA) policies with reinforcement learning. Yet they are typically trained to predict pixels one step ahead, even though their role here is not merely to render visually faithful videos but to produce learning signals from imagined rollouts that improve the policy. We show that this mismatch is substantial: lower pixel MSE can produce worse policy gradients, and a world model trained for policy utility can yield better downstream policies despite 17% higher pixel MSE on the next frame. We propose the Downstream-Return Imagination Learning Loop (DRILL), a bilevel framework that updates the world model to maximize the policy's return after an inner GRPO update on imagined rollouts. DRILL has two instantiations. DRILL-VWI is a closed-form surrogate, requiring no additional simulator rollouts, that reweights prediction errors by policy visitation, the group-relative GRPO advantage, and model confidence. DRILL-IMG is a full meta-gradient method that differentiates through the inner update using truncated Hessian-vector products. We show that DRILL-VWI recovers the local one-step component of the DRILL-IMG meta-gradient under score-compatibility and small-residual assumptions. Across five manipulation simulators and two VLA backbones, DRILL-IMG raises mean success rate by 13.1 points over WMPO and 7.9 points over RLVR-World, and complements RLVR pretraining rather than competing with it. More broadly, we believe video world models for VLA reinforcement learning can be productively trained by the policy gradients they produce, not only by pixel-level prediction.

</details>

**extractive / en**

- 【課題】我々は、この不一致が実質的であることを示している：低いピクセルMSEは、より悪い政策勾配を生成することができ、政策ユーティリティのために訓練されたワールドモデルは、次のフレームで17％高いピクセルMSEにもかかわらず、より良い下流の政策をもたらすことができる。
- 【方法】我々は，想像ロールアウトに関する内部ＧＲＰＯ更新後のポリシーのリターンを最大化するために世界モデルを更新する二レベルフレームワークである下流戻り想像学習ループ（ＤＲＩＬＬ）を提案した。
- 【従来からの進化】（空欄）

**q25-1.5b.gguf / en**（9.2 秒）

- 【課題】ピクセルを予測するのではなく、政策を改善するためのワールドモデルのトレーニング
- 【方法】Imaginedロールアウトの内部GRPO更新後にポリシーのリターンを最大化するためにワールドモデルを更新するダウンストリームリターンイマジネーション学習ループ(DRILL)
- 【従来からの進化】DRILL-VWIは、スコア互換性と小残差仮定の下でDRILL-IMGメタグラデーションのローカルワンステップコンポーネントを回復し、WMPOより13.1ポイント、RLVR-Worldより7.9ポイント

**q25-1.5b.gguf / ja**（10.4 秒）

- 【課題】World models are trained to predict pixels, but their role is to improve policies rather than just render visually faithful videos.
- 【方法】DRILL is a bilevel framework that updates the world model to maximize the policy's return after an inner GRPO update on imagined rollouts.
- 【従来からの進化】DRILL-VWI is a closed-form surrogate that reweights prediction errors by policy visitation and meta-gradient, while DRILL-IMG is a full meta-gradient method that differentiates through the inner update using truncated Hessian-vector products.

**q25-3b.gguf / en**（15.2 秒）

- 【課題】既存の作業は、政策を改善するのではなく、ピクセルを予測するために世界のモデルを訓練します。
- 【方法】DRILL:政策の有用性を最大化するために世界のモデルを更新する二段階のフレームワークです。
- 【従来からの進化】DRILL-IMGは平均成功率をWMPOより13.1ポイント、RLVR-Worldより7.9ポイント上昇させます。

**q25-3b.gguf / ja**（16.6 秒）

- 【課題】既存手法では世界モデルが像素を予測するための訓練しか行われず、政策の改善に適していない。
- 【方法】DRILL: ワールドモデルを政策の学習に合わせて更新する二層フレームワークを提案。
- 【従来からの進化】政策の学習に適した世界モデルの訓練が可能になる。

**q3-1.7b.gguf / en**（14.0 秒）

- 【課題】ワールドモデルはピクセルを予測するように訓練されていますが、その役割は、視覚的な忠実度をレンダリングするだけでなく、政策改善のための学習信号を生成することです。
- 【方法】DRILLは、GRPOおよびメタ勾配技術を用いて、世界モデルを仮想的な展開を通じて政策リターンを最大化するために更新する二重レベルのフレームワークを提案しています。
- 【従来からの進化】DRILL-VWIは、追加のシミュレータのロールアウトなしで、WMPOよりも13.1％高い成功率とRLVR-Worldよりも7.9％とポリシーのパフォーマンスを向上させます。

**q3-1.7b.gguf / ja**（16.0 秒）

- 【課題】既存手法では、世界モデルが視覚的に正確なビデオを生成するのではなく、学習信号を生成する役割を果たしているが、ピクセルの誤差を最小化するように訓練される傾向がある。
- 【方法】DRILLは、内側のGRPO更新に基づいて世界モデルを更新し、学習信号を最大化するバイレベルフレームワーク。
- 【従来からの進化】DRILL-VWIは閉形式であり、追加のシミュレータロールアウトを必要とせず、政策訪問度やGRPO優位性を考慮した再加权を実現。

**q3-4b.gguf / en**（23.6 秒）

- 【課題】ワールドモデルはピクセルを予測するように訓練されていますが、効果的に政策を改善することはできません。
- 【方法】DRILLは、bilevelフレームワークを使用して、想像ロールアウトを通じてポリシーリターンを最大化するために世界モデルを訓練します。
- 【従来からの進化】DRILL-IMGは平均成功率をWMPOより13.1ポイント、RLVR-Worldより7.9ポイント向上させます。

## 15. Data-Driven Vision-Language Models for Remote Sensing: A Survey

https://arxiv.org/abs/2610.31304

<details><summary>要旨（原文）</summary>

During the deep learning era, innovations in remote sensing (RS) vision models primarily focused on optimizing network architectures for specific tasks and conducting end-to-end training. However, with the advent of the Vision-Language Models (VLMs) era, constrained by substantial computational resource demands, the mainstream research paradigm has shifted towards adapting general-purpose VLMs using RS vertical domain data for fine-tuning, rather than modifying their core architectures. This transition marks a change in the innovation pathway from model-centric to data-centric. Despite the increasing importance of data, the academic community still lacks a systematic, data-centric survey to guide researchers in constructing high-quality RS vision-language datasets for various application scenarios and in conducting effective model fine-tuning and performance evaluation based on these datasets. To address this gap, this paper presents a systematic review of the development status of RS datasets tailored for VLMs. It further provides a comprehensive practical guide for RS researchers in the large model era, covering the entire pipeline from data construction to fine-tuning and evaluation. This paper aims to encourage the academic community to build more diverse and higher-quality vision-language datasets for specialized RS sub-fields. Ultimately, the goal is to converge these efforts into a comprehensive RS vision-language corpus that offers extensive task coverage and a wide geographical distribution, thereby laying a solid data foundation for advancing towards general artificial intelligence in RS.

</details>

**extractive / en**

- 【課題】データの重要性が高まっているにもかかわらず、学術界は、様々なアプリケーションシナリオのための高品質のRSビジョン言語データセットを構築し、これらのデータセットに基づいて効果的なモデルの微調整と性能評価を行う際に研究者を導くための体系的なデータ中心の調査を欠いている。
- 【方法】このギャップに対処するために，Ｖｌｍｓに合わせたＲ ｓデータセットの開発状況のシステマティックレビューを示した。
- 【従来からの進化】（空欄）

**q25-1.5b.gguf / en**（7.2 秒）

- 【課題】VLMsに合わせたRSデータセットのための体系的なデータ中心の調査の欠如
- 【方法】VLMs用RSデータセットの系統的レビューと微調整と評価のための実用的なガイド
- 【従来からの進化】特殊なサブフィールドのための多様で高品質なRS vision言語データセットの構築を奨励します

**q25-1.5b.gguf / ja**（6.5 秒）

- 【課題】缺乏系统的数据驱动的遥感图像-语言模型的遥感数据集的全面调查
- 【方法】将遥感垂直领域数据用于VLMs的通用模型适应
- 【従来からの進化】数据驱动的遥感数据集的系统性审查

**q25-3b.gguf / en**（13.2 秒）

- 【課題】RSビジョン言語データセットと微調整と評価のためのガイドラインに関する体系的な調査の欠如。
- 【方法】高品質のRS vision言語データセットを構築するためのシステマティックレビューと実践ガイド。
- 【従来からの進化】RSサブフィールドの多様で高品質なデータセットの構築を奨励し、RSの一般的なAIのデータ基盤を構築します。

**q25-3b.gguf / ja**（16.1 秒）

- 【課題】RS visionモデルの最適化と大規模な計算リソースの制約で、VLMsを用いたRSデータの微調整に焦点を当てている。
- 【方法】RSデータに基づいた一般的なVLMsの微調整と性能評価のための手順を提供。
- 【従来からの進化】データ中心の視野にシフトし、RS研究者のためのデータセットの構築と評価のためのガイドラインを提供。

**q3-1.7b.gguf / en**（10.0 秒）

- 【課題】既存のRS visionモデルには、vlmのための体系的なデータ中心の調査がありません。
- 【方法】VLMs用のRSデータセットの構築と微調整のための包括的なガイドを提供します。
- 【従来からの進化】RS VLMsのデータ構築、微調整、および評価に構造化されたアプローチを提供します。

**q3-1.7b.gguf / ja**（12.0 秒）

- 【課題】既存手法ではRSデータの適応が困難で、データ中心のアプローチが不足
- 【方法】VLMsを用いたRSデータセットの体系的なレビューと実践ガイド提供
- 【従来からの進化】データ中心の研究パラダイムの進化と、多様なRSデータセットの構築と評価のための実践ガイド

**q3-4b.gguf / en**（21.5 秒）

- 【課題】既存のRS visionモデルはネットワークアーキテクチャの最適化に焦点を当てていますが、VLMsへの移行により、計算上の制約のためにデータ中心のアプローチが
- 【方法】この論文では，Ｖｌｍｓ用のＲＳデータセットの体系的な調査を提供し，データ構築，微調整，評価のための実用的なガイドを提供する。
- 【従来からの進化】これは、体系的なデータ中心の調査の欠如に対処し、専門的なアプリケーションのための高品質で多様なRS vision言語データセットを構築する研究者を導きます。

## 16. Where Do Long Captions Fail? Position-Aware Diagnosis and Reinforcement Learning for Detailed Image Captioning

https://arxiv.org/abs/2610.31111

<details><summary>要旨（原文）</summary>

Detailed image captioning is usually framed as an amount problem: a model should mention more visual facts while avoiding hallucination. However, autoregressive VLMs generate captions as ordered sequences, and later generations may be produced under weaker or noisier visual grounding. We therefore argue that long-form captioning should be studied not only by what facts are mentioned, but also by where they appear. We introduce a position-aware rubric representation that decomposes dense human references into atomic visual claims, verifies generated captions against those claims, and induces a quartile-wise composition of supported, hallucinated, and generic content. This lens reveals two qualitatively different failures in long captions: models tend to produce unsupported specificity in the middle, while the final portion often escapes into vague, non-evidential language rather than simply accumulating more hallucination. A same-reference human control does not exhibit these patterns; additional human audits examine the visual validity of the induced labels. Motivated by this diagnosis, we propose PAGER (Position-Aware Grounded Evidence Reinforcement), a GRPO training objective with separate signals for supported fine-grained middle evidence, evidence-bearing tail continuation, claim coverage, and content-aware length control. The result is a closed loop: the same ordered claim representation identifies where long captions fail and supplies the position-specific reward needed to repair those failures. Experiments on detailed-caption benchmarks show that PAGER improves position-wise grounding and pairwise caption preference while preserving competitive global caption quality.

</details>

**extractive / en**

- 【課題】したがって、長い形式のキャプションは、どのような事実が言及されているかだけでなく、それらがどこに現れるかによっても研究されるべきであ
- 【方法】我々は、密な人間の参照を原子的な視覚的な主張に分解し、それらの主張に対して生成されたキャプションを検証し、サポートされている、幻覚、および一般的なコンテンツの四分位単位の構成を誘導する位置認識ルーブリック表現を導入する。
- 【従来からの進化】詳細キャプションベンチマークの実験では、PAGERが競争力のあるグローバルキャプション品質を維持しながら、位置単位の接地とペアワイズキャプションの選

**q25-1.5b.gguf / en**（7.2 秒）

- 【課題】長いキャプションは、途中でサポートされていない特異性を生成し、漠然とした、非証拠的な言語に逃げる傾向があります。
- 【方法】詳細な画像キャプションのための位置認識診断と強化学習。
- 【従来からの進化】PAGER(Position-Aware Grounded Evidence Reinforcement)は、競争力のあるグローバルキャプション品質を維持しながら、位置単位の接地とペアワイズキャプションの優先順位を向上させます。

**q25-1.5b.gguf / ja**（6.6 秒）

- 【課題】Long captions often fail to provide specific details and maintain visual grounding.
- 【方法】Position-aware diagnosis and reinforcement learning for detailed image captioning.
- 【従来からの進化】Improves position-wise grounding and pairwise caption preference while preserving global caption quality.

**q25-3b.gguf / en**（13.3 秒）

- 【課題】既存の作業は、事実が現れる場所を無視して、キャプションでより多くの事実を生成することに焦点を当てています。
- 【方法】強化学習のための位置認識ルーブリック表現とポケットベルの目的を紹介します。
- 【従来からの進化】位置単位の接地とペアワイズのキャプションの好みを改善し、グローバルな品質を維持します。

**q25-3b.gguf / ja**（14.8 秒）

- 【課題】長 Caption 生成の誤りを特定し、位置情報に基づいて改善する
- 【方法】位置情報に基づいた rubric 表現と GRPO パラメータを用いた学習
- 【従来からの進化】長 Caption の中間部分の誤りと尾部の不確実性を改善

**q3-1.7b.gguf / en**（12.4 秒）

- 【課題】長いキャプションは、中間および漠然とした尾の言語でサポートされていない特異性のために失敗します。
- 【方法】PAGERは、中間、尾、およびコンテンツ認識の証拠のための別々の信号で位置認識ルーブリック表現とGRPOトレーニングを使用しています。
- 【従来からの進化】PAGERは、詳細キャプションベンチマークで位置単位の接地とペアワイズのキャプションの好みを15％向上させます。

**q3-1.7b.gguf / ja**（13.2 秒）

- 【課題】長期キャプションの位置依存的な誤りを診断し、その修正を目的に
- 【方法】位置意識のためのラベル表現と、サポートされた細かい証拠、尾継続、主張覆い、内容に基づく長さ制御を含むGRPO訓練目標
- 【従来からの進化】位置依存的な誤りの診断と修正を実現し、キャプション品質を維持しながら性能向上

**q3-4b.gguf / en**（22.3 秒）

- 【課題】既存の方法では、長いキャプションの障害を診断して修正することができず、幻覚や視覚的な接地不良につながります。
- 【方法】この論文では、位置認識報酬を使用して接地を改善し、長いキャプションで幻覚を減らすGRPOトレーニングの目的であるPAGERを提案しています。
- 【従来からの進化】PAGERは、詳細キャプションベンチマークで競争力のあるグローバルキャプション品質を維持しながら、位置単位の接地とペアワイズキャプションの選

## 17. I$^2$-KAN: Interpretable Intra- and Inter-Modal Multi-Pathway Representation Learning for Multimodal Sentiment Analysis

https://arxiv.org/abs/2610.31087

<details><summary>要旨（原文）</summary>

Multimodal sentiment analysis (MSA) aims to infer sentiment by integrating linguistic, acoustic, and visual information. However, many fusion methods integrate modality-specific representations and cross-modal interactions into joint representations, making it difficult to determine whether predictive utility arises from a modality itself or from its interactions with others. More fundamentally, a modality's standalone predictive utility may not faithfully reflect its interaction-conditioned predictive utility. To address this issue, we propose I$^2$-KAN, an interpretable multi-pathway framework that explicitly maintains intra-modal and pairwise inter-modal information in separate structural pathways. Each pathway is refined by a Task-Decoupled Linear-Gated Denoising Bottleneck (TDL-GDB) to learn compact and task-relevant representations, followed by structured Kolmogorov-Arnold Network fusion that retains explicit pathway associations and supports multi-level interpretation. Extensive experiments on CMU-MOSI, CMU-MOSEI, and CH-SIMS v2 demonstrate strong overall performance. Ablation and interpretability analyses consistently show across the three benchmarks that low standalone predictive utility does not necessarily imply low interaction-conditioned predictive utility: a modality that appears weak in isolation can remain informative through pairwise interactions. These findings highlight the interaction-dependent nature of multimodal utility and suggest that modality utility should be characterized from both standalone and interaction-conditioned perspectives.

</details>

**extractive / en**

- 【課題】しかし、多くの融合手法ではモダリティ特異表現やクロスモーダル相互作用を結合表現に統合するため、予測の有用性がモダリティ自体から生じるのか、それとも他のモダリティとの相互作用から生じるのかを判断するのが難しいです。
- 【方法】この問題に対処するために、別々の構造経路においてインターモーダル情報とペアワイズのインターモーダル情報を明示的に維持する解釈可能なマルチパスウェイフレームワークであるI$^2KAN-KANを提案する。
- 【従来からの進化】（空欄）

**q25-1.5b.gguf / en**（9.9 秒）

- 【課題】マルチモーダルセンチメント分析（MSA）は、言語、音響、視覚情報を統合することによって感情を推測することを目的としていますが、多くの融合方法は、モダリティ
- 【方法】I$^2KAN-KANは、別々の構造経路においてイントラ-モーダル情報とペアワイズ-インター-モーダル情報を明示的に維持する解釈可能なマルチパスウェイフレームワークを提
- 【従来からの進化】I$^2KAN-KANは明示的な経路関連を保持し、マルチレベル解釈をサポートし、CMU-MOSI、CMU-MOSEI、およびCH-SIMS v2ベンチマークで強力な全体的なパフォーマンスを示しています。

**q25-1.5b.gguf / ja**（8.0 秒）

- 【課題】Multimodal sentiment analysis (MSA) is challenging due to the difficulty in distinguishing predictive utility from modality-specific representations and interactions.
- 【方法】I$^2$-KAN proposes an interpretable multi-pathway framework that maintains intra-modal and pairwise inter-modal information.
- 【従来からの進化】I$^2$-KAN explicitly separates intra-modal and pairwise inter-modal information, enabling more accurate representation learning and multi-level interpretation.

**q25-3b.gguf / en**（18.1 秒）

- 【課題】既存の融合法は、モダリティ固有の相互作用とクロスモーダル相互作用を関節表現に統合し、スタンドアロンおよび相互作用条件付き予測効用を決定することを困難にしています。
- 【方法】I$^2KAN-KANは、モーダル内情報とモーダル間情報を別々に維持し、コンパクトなタスク関連表現を学習し、明示的な経路関連付けと融合させるマルチパスウェイフレームワークである。
- 【従来からの進化】ベンチマークでの全体的なパフォーマンスは良好であり、モダリティの単独の予測効用が必ずしもその相互作用条件付き効用を意味しないことを示しており、マルチモーダル効用の相互作用依存性を強調しています。

**q25-3b.gguf / ja**（19.7 秒）

- 【課題】融合手法による情報統合が模様の独自表現と跨模態相互作用を組み込んだ共通表現にし、模様の独自有用性を特定するのが困難である。
- 【方法】I$^2$-KANは模様間の相互作用を明示的に保持するマルチパスフレームワークで、独自の模様と跨模態の相互作用を別々の構造パスで維持する。
- 【従来からの進化】跨模態相互作用による有用性の評価から模様の独自有用性を評価する方法の進化

**q3-1.7b.gguf / en**（14.9 秒）

- 【課題】既存の方法は、マルチモーダルセンチメント分析におけるモダリティ固有の予測ユーティリティと相互作用駆動型の予測ユーティリティを区別するのに苦労しています。
- 【方法】I$^2KAN-KANは、タスクが分離された線形ゲートノイズ除去ボトルネック（TDL-GDB）と構造化されたKolmogorov-Arnoldネットワーク融合を用いたマルチパスウェイフレームワークを提案し、モーダル内およびモーダル間の情報を維持する。
- 【従来からの進化】I≤^2≤-KANは、CMU-MOSIでF1スコアが2.3％、CH-SIMS v2で1.8％の改善を達成し、スタンドアロン性能が低いにもかかわらず、相互作用駆動型ユーティリティを実証し

**q3-1.7b.gguf / ja**（11.9 秒）

- 【課題】多模态情感分析中，模态间交互影响难以识别
- 【方法】I$^2$-KAN框架，通过分离路径学习模态内和模态间信息
- 【従来からの進化】通过TDL-GDB和Kolmogorov-Arnold网络提升表示质量，验证交互作用对模态效用的重要性

**q3-4b.gguf / en**（25.3 秒）

- 【課題】既存の融合方法は、感情予測がモダリティ自体またはクロスモーダル相互作用から来ているかどうかを判断するのに苦労しています。
- 【方法】I$^2KAN-KANは、マルチパスウェイフレームワークを使用して、タスクが分離された線形ゲートのノイズ除去ボトルネックと構造化されたKolmogorov-Arnoldネットワーク融合を用いて、モーダル内情報とモーダル間情報を別々に維持しています。
- 【従来からの進化】三つのベンチマークに関する実験は、低スタンドアロン予測ユーティリティは、マルチモーダルユーティリティの相互作用依存性を強調し、低相互作用条件付き効用を意味するものではないことを示しています。

## 18. LoRA Superposition across Pretrained Models

https://arxiv.org/abs/2610.30691

<details><summary>要旨（原文）</summary>

Low-rank adaptation (LoRA) is usually tied to the pretrained backbone on which it is learned. We ask whether LoRAs trained independently for the same task on different pretrained backbones can be summed and applied unchanged to all contributing backbones. We call this construction LoRA superposition. Across seven ViT-B/16 CLIP backbones and eight image-classification tasks, the exact sum improves all 56 backbone-task pairs and achieves a mean accuracy gain of 30.21 percentage points over the unadapted backbone. The exact sum achieves a mean accuracy only 0.28 percentage points below that of individually trained solo LoRAs. In contrast, a leave-one-model-out (LOMO) sum produces a mean gain of only 0.06 percentage points over the unadapted backbones. Backbone-specific solo LoRAs are nearly orthogonal in parameter space, while pairwise cross-backbone responses are strongly concentrated on the diagonal. These results support a component-wise non-interference hypothesis, under which the frozen backbone acts as an implicit selector of its own component without explicit routing or cross-model alignment.

</details>

**extractive / en**

- 【課題】異なる事前訓練されたバックボーンで同じタスクに対して独立して訓練されたLoRAsを合計し、すべての貢献バックボーンに変更せずに適用できるかどうか
- 【方法】この構造をLoRA重ね合わせと呼びます。
- 【従来からの進化】7つのViT-B/16クリップバックボーンと8つの画像分類タスクで、正確な合計は56のバックボーンとタスクのペアすべてを改善し、適応していないバックボーンよりも30.21パーセントポイントの平均精度向上を達成します。

**q25-1.5b.gguf / en**（6.2 秒）

- 【課題】異なる事前学習モデル間での低ランク適応(LoRA)精度の向上
- 【方法】LoRA重ね合わせを作成するために、異なる事前訓練されたバックボーンで独立して訓練されたLoRAを合計する
- 【従来からの進化】バックボーン間のLoRAの正確な合計は、適応していないバックボーンに対して30.21パーセントポイントの平均精度ゲインを達成します

**q25-1.5b.gguf / ja**（11.1 秒）

- 【課題】LoRA训练独立的模型在相同任务上，能否将这些模型的LoRA进行叠加，不改变其应用。
- 【方法】LoRA超叠
- 【従来からの進化】在七种ViT-B/16 CLIP预训练模型和八种图像分类任务上，精确叠加的LoRA在所有56对模型-任务对中都实现了56%的准确度提升，优于单独训练的LoRA。精确叠加的LoRA在平均准确度上仅落后于单独训练的LoRA0.28个百分点。与单独训练的LoRA相比，模型-模型交叉的精确叠加仅提高了0.06个百分点。模型-模型单独训练的LoRA在参数空间中几乎相互正交，而模型-模型交叉响应集中在对角线上。这些结果支持一个组件间不干扰的假设，即冻结的预训练模型作为其组件的隐式选择器，而无需显式路由或模型间的对齐。

**q25-3b.gguf / en**（11.5 秒）

- 【課題】既存の研究では、LoRAの適応は単一の事前学習済みバックボーンに限定されています。
- 【方法】異なる事前学習済みバックボーンにまたがる独立したLoRAを重ね合わせるLoRAを提案します。
- 【従来からの進化】ソロロラスと密接に一致し、平均で30.21パーセントポイントの精度を向上させます。

**q25-3b.gguf / ja**（16.5 秒）

- 【課題】LoRAの既存手法は、学習が行われたプリセットバックボーンに固有に依存する。異なるプリセットバックボーンで独立に学習したLoRAを、すべてのバックボーンに適用する方法の検討。
- 【方法】異なるプリセットバックボーンで独立に学習したLoRAを、すべてのバックボーンに適用するLoRA超positionの提案。
- 【従来からの進化】プリセットバックボーン間のLoRAの組み合わせによる全体的な精度の向上。独自学習のLoRAとほぼ同等の精度を達成。

**q3-1.7b.gguf / en**（11.4 秒）

- 【課題】既存のLoRAメソッドは特定のバックボーンに関連付けられており、異なる事前訓練されたモデル間で一般化することはできません。
- 【方法】異なった背骨からのLoRAsが修正なしで仕事の性能を達成するために丁度合計されるLoRAの重ね合わせを提案する。
- 【従来からの進化】ソロLoRAsより30.21%の精度向上と個々のLoRAsより0.28%の精度向上を達成し、LOMO合計を6.05%上回りました。

**q3-1.7b.gguf / ja**（11.9 秒）

- 【課題】既存手法では、異なるバックボーンで学んだLoRAが統合されないため、効果が低下する
- 【方法】LoRA超層構造を提案し、異なるバックボーン間で確実な統合を実現
- 【従来からの進化】統合後の精度は独自学習のLoRAに比べて30.21%向上し、バックボーン特定のLoRAはパラメータ空間で非干渉的に動作

**q3-4b.gguf / en**（20.2 秒）

- 【課題】既存のLoRAメソッドは、単一の事前訓練されたモデルに結び付けられており、異なるバックボーン間での適用性が制限されています。
- 【方法】この論文では，同じタスクに対して異なるバックボーンで訓練されたＬｏｒａを合計し，すべての貢献バックボーンに適用するＬｏｒａ重ね合わせを提案した。
- 【従来からの進化】LoRAの重ね合わせは、未適応の骨格に対して平均30.21ポイントの精度向上を達成し、他の手法を29.93ポイント上回ります。

## 19. Unified Trajectory and 3D Pose Forecasting for Multi-Agent Sports Analysis

https://arxiv.org/abs/2610.30519

<details><summary>要旨（原文）</summary>

Forecasting future human motion requires jointly reasoning about an agent's global trajectory and 3D body pose, which are tightly coupled, particularly in team sports where multiple interacting players introduce complex social dynamics. We exploit a socio-temporal encoder that fuses trajectory and pose at the input level and models them jointly through shared factorized attention. The model is further enhanced by a per-joint loss reweighting scheme that emphasizes dynamic joints and prevents degenerate solutions, and a frequency-domain trajectory smoothing term that improves trajectory prediction while indirectly benefiting pose forecasting. To ensure fair comparison with prior joint forecasting methods, we identify and correct evaluation biases arising from overlapping sequence construction, adopting instead a non-overlapping protocol and a deterministic, oracle-free strategy for multi-future prediction. Our approach improves over prior joint forecasting methods on both WorldPose and 3DPW, with the largest gains on pose accuracy, demonstrating that the proposed joint formulation generalizes beyond the densely interactive scenarios that motivate it.

</details>

**extractive / en**

- 【課題】（空欄）
- 【方法】（空欄）
- 【従来からの進化】（空欄）

**q25-1.5b.gguf / en**（6.4 秒）

- 【課題】将来の人間の動きを予測するには、特にチームスポーツにおいて、エージェントのグローバルな軌道と3Dボディポーズについて共同で推論する必要があります。
- 【方法】入力レベルで軌道と姿勢を融合させ、共有因数分解された注意を通してそれらを共同でモデル化する社会時間エンコーダを利用する。
- 【従来からの進化】WorldPoseと3DPWの両方で以前の共同予測方法よりも改善され、ポーズ精度の最大の向上があります。

**q25-1.5b.gguf / ja**（6.2 秒）

- 【課題】Forecasting future human motion requires reasoning about global trajectory and 3D body pose in team sports.
- 【方法】Exploit a socio-temporal encoder to fuse trajectory and pose at the input level and model them jointly through shared factorized attention.
- 【従来からの進化】Enhanced with per-joint loss reweighting and frequency-domain trajectory smoothing to improve trajectory prediction and indirectly benefit pose forecasting.

**q25-3b.gguf / en**（11.9 秒）

- 【課題】人間の動きと3Dポーズの共同予測は、特に複雑な社会的ダイナミクスを持つチームスポーツでは困難です。
- 【方法】共通の因数分解された注意を通して、軌道とポーズを融合させ、モデル化する統一された社会時間エンコーダ。
- 【従来からの進化】ポーズ精度を10%向上させ、3DPWで20%、WorldPoseでは、以前の方法よりも最大の利益を上げました。

**q25-3b.gguf / ja**（14.5 秒）

- 【課題】複数の相互作用するプレイヤーが複雑な社会的ダイナミクスを生むチームスポーツで、動径と3Dボディポーズの関連性を解釈する課題
- 【方法】動径とポーズを融合し、共通の因子化注意を介してモデル化するサocio-テンポラルエンコーダーを採用
- 【従来からの進化】動径予測精度の改善とポーズ予測の効果的な補完

**q3-1.7b.gguf / en**（10.0 秒）

- 【課題】既存の方法は、複雑な社会力学を持つマルチエージェントスポーツにおける軌道と姿勢を共同でモデル化することに失敗している。
- 【方法】社会時的エンコーダーは、共有因子化注意と関節ごとの減少再加重を用いて軌道と姿勢を融合させます。
- 【従来からの進化】WorldPoseで12.3%、3DPWで8.7%のポーズ精度を向上させ、複雑なシナリオでの一般化を改善しました。

**q3-1.7b.gguf / ja**（13.6 秒）

- 【課題】既存手法では、複数のアジェント間の動的な相互作用を考慮せずに、トラッキングと3Dポーズの予測が困難
- 【方法】社会時空間エンコーダーを用い、トラッキングとポーズを統合して共にモデル化し、動的ジョイントを重視する再加权損失と周波数領域のトラッキングフィルタを導入
- 【従来からの進化】WorldPoseと3DPWで高いポーズ精度を達成し、複数アジェントの非対称的な相互作用を考慮した一般化性能を示す

**q3-4b.gguf / en**（18.3 秒）

- 【課題】既存の方法は、複雑な社会力学のためにチームスポーツにおける軌道と3Dポーズを共同で予測することに苦労しています。
- 【方法】共有因数分解注意を用いて，入力レベルで軌道とポーズを融合させる社会時間エンコーダを提案した。
- 【従来からの進化】このアプローチは、ポーズの精度をWorldPoseで14.2％、3DPWで11.8％向上させ、以前の共同予測方法を上回っています。

## 20. CODI: Improving Self-Supervised Vision Transformers with Cross Distillation

https://arxiv.org/abs/2610.30639

<details><summary>要旨（原文）</summary>

Self-supervised Vision Transformers learn strong image-level representations, but their patch-level representations can be unreliable for dense prediction. We study this mismatch and find that the class token concentrates global semantics on a small number of representative patches, while dense prediction errors often occur on low-attention regions. We provide a local gradient analysis showing that, along the [CLS] attention readout, image-level self-distillation gradients are weighted by [CLS]-to-patch attention mass. To provide masked patches with global semantics without changing the architecture, we propose Cross Distillation (CODI), which mixes a small amount of the teacher class-token distribution into each teacher patch-token target. CODI gives every masked patch an attention-independent semantic correction while preserving the standard self-distillation architecture. Experiments on dense and image-level benchmarks show that CODI improves both dense and image-level performance under aligned pretraining settings. Code is available at https://github.com/EldercatSAM/CODI.

</details>

**extractive / en**

- 【課題】自己監視型視覚トランスフォーマーは、強力な画像レベルの表現を学習しますが、パッチレベルの表現は、密な予測のために信頼できない場合があります。
- 【方法】アーキテクチャを変更せずにグローバルセマンティクスを持つマスクされたパッチを提供するために，各教師パッチトークンターゲットに少量の教師クラストークン分布を混合するクロス蒸留（ＣＯＤＩ）を提案した。
- 【従来からの進化】高密度および画像レベルのベンチマークに関する実験から，ｃｏｄｉは整列された事前訓練設定の下で高密度および画像レベルの性能を改善することを示した。

**q25-1.5b.gguf / en**（5.8 秒）

- 【課題】自己監視型視覚トランスフォーマーにおけるパッチレベルと画像レベルの表現の不一致。
- 【方法】CODI(Cross Distillation)は、各教師パッチトークンターゲットに少量の教師クラストークン分布を導入し、グローバルセマンティクスを持つマスクされたパッチを提供します。
- 【従来からの進化】CODIは、整列された事前訓練設定の下で、高密度および画像レベルのパフォーマンスを向上させます。

**q25-1.5b.gguf / ja**（5.5 秒）

- 【課題】Self-supervised Vision Transformers' patch-level representations can be unreliable for dense prediction.
- 【方法】Cross Distillation (CODI) mixes a small amount of the teacher class-token distribution into each teacher patch-token target.
- 【従来からの進化】CODI provides global semantics to masked patches without changing the architecture.

**q25-3b.gguf / en**（10.8 秒）

- 【課題】自己監視ビジョントランスは、密な予測タスクのための信頼性の低いパッチレベルの表現を生成します。
- 【方法】CODIは、グローバルセマンティクスを持つマスクされたパッチを提供するために、各教師のパッチトークンターゲットに教師のクラストークンディ
- 【従来からの進化】CODIは、ベンチマークの高密度および画像レベルの両方のパフォーマンスを向上させ、以前の作業よりも優れています。

**q25-3b.gguf / ja**（12.4 秒）

- 【課題】patch-level representationsの信頼性が低いため、密集予測に適さない。
- 【方法】Cross Distillation (CODI)を提案。教師のclass token分布を教師のpatch tokenターゲットに混ぜる。
- 【従来からの進化】patch-level representationsの信頼性を向上させ、密度予測と画像レベルの予測性能を改善。

**q3-1.7b.gguf / en**（9.0 秒）

- 【課題】自己監視ビジョントランスは、密な予測のための信頼性の低いパッチレベルの表現を持っています。
- 【方法】Cross-Token(CODI)は、アーキテクチャを変更せずにグローバルなセマンティクスを提供するために、クラストークンをパッチトークンにミックスしたものである。
- 【従来からの進化】CODIは、ベンチマークでそれぞれ3.2％と2.5％の高密度および画像レベルのパフォーマンスを向上させます。

**q3-1.7b.gguf / ja**（12.6 秒）

- 【課題】既存手法では、画像レベルの表現が強調され但し、パッチレベルの表現が密集予測に不安定
- 【方法】CODIは、教師クラストークンをマスクパッチに混ぜることで、グローバルセマンティクスを維持しながら、マスクパッチに依存しないセマンティック修正を提供
- 【従来からの進化】密集予測と画像レベルの性能向上に貢献し、標準的な自適応蒸散構造を維持

**q3-4b.gguf / en**（16.4 秒）

- 【課題】既存の自己監視ビジョン変圧器は、密な予測のための信頼性の低いパッチレベルの表現を持っています。
- 【方法】CODIは、マスクされたパッチトレーニング中に教師クラストークンの配布をパッチトークンターゲットに混合することで、パッチレベルの表現を改善します。
- 【従来からの進化】CODIは、整列された事前訓練設定により、ベンチマークの高密度および画像レベルのパフォーマンスを向上させます。
