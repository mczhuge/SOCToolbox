# SOC快速评测工具

## News:

🔥🔥🔥 **100个模型在SOC的显著图可以在此下载**  [Here](https://drive.google.com/drive/folders/1E80KZiyEoxxR6lqe3x8SSar6gYYm9xkf)!

## 1. 数据集与训练设置 [可忽略，直接跳到 2.评估，此仅为说明训练的设置]

值得注意的是，在[ICON (arXiv, 2021）](https://arxiv.org/pdf/2101.07663.pdf)中， 我们使用了以下训练设置:

- 同时使用train和val集合来训练, 以获得最高效性能. 
- 除此之外, 训练、测试时, 丢弃了没有显著物体的图片(gt为空白).

因此, 我们ICON模型的训练和测试图像数目分别为2400和600张.

方便起见, 可通过 [百度网盘 | 提取码: iqul ](https://pan.baidu.com/s/1kWebPUhCQOCsvvAouo7eGQ)，直接下载我们划分好的SOC。然后像训练DUTS一样去训练SOC数据集。

**如果你通过以上链接下载SOC, 可直接忽略以下步骤.**

----

你也可以参考如下方法，来获得与上边一样的数据集：

(A) 生成 train.txt 列表，列表里的图片名称对应的图片都是包含显著物体的(非空白图)。


```
python ./Train/SOC/drop_blank_and_generate_list.py 
```

(B) 划分9个特殊类别并且生成它们对应的 test.txt 列表:

```
python ./Test/SOC/attr_categoty_and_generate_list.py 
```

然后， 将会产生9个包含不同属性的划分文件夹，这一步很重要，因为划分好后的文件夹不仅利于 SOCToolbox 评估模型性能，也能方便您分析不同类别。产生的文件夹包含RGB images和对应GTs是依次是: `./maps/GT/SOC/Test/SOC-AC`, `./maps/GT/SOC/Test/SOC-BO`, `./maps/GT/SOC/Test/SOC-CL`, `./maps/GT/SOC/Test/SOC-HO`, `./maps/GT/SOC/Test/SOC-MB`, `./maps/GT/SOC/Test/SOC-OC`, `./maps/GT/SOC/Test/SOC-OV`, `./maps/GT/SOC/Test/SOC-SC`,`./maps/GT/SOC/Test/SOC-SO`. 

**实际上, 如果你是通过上述链接下载的SOC数据集, 我们已经搞定了A,B两步骤.** (必要时, 你可以找到原始SOC数据集, 在 [这里](https://dpfan.net/socbenchmark/), 然后做上述A和B.)

## 2. 评估

如果你训练已经完成, 需要生成`SOC-AC`, `SOC-BO`, `SOC-CL`, `SOC-HO`, `SOC-MB`, `SOC-OC`, `SOC-SC`, `SOC-OV`, `SOC-SC`和 `SOC-SO` 对应的预测图。

如果你很早就已经生成了所有的SOC-Test, 可以通过把 `Attributes` 文件夹添加至你的预测文件夹, 如 `./maps/Prediction/你的模型/SOC/Attributes` 然后稍微改动一下这个 `./maps/Prediction/你的模型/SOC/attr_categoty_and_generate_list.py`里的路径, 就可以自动的划分9个属性的预测图到9个不同的文件夹。

然后, 变更run_eval中的METHOD='你的模型'，就可以开始评估了, 时长大约在2分钟左右.

```
sh run_eval.sh
```

## 3. 结果展示
[ICON](https://arxiv.org/pdf/2101.07663.pdf) 模型的显著图可到 [Baidu | 提取码:bopg](https://pan.baidu.com/s/19XV19I_0gfAjx2gwcweZcw)下载.

以下为使用SOCToolbox评估的结果:

Tranined on DUTS, evaluated on SOC-Attr(9 attributes, 600 pics)
```
Method:ICON,Dataset:SOC,Attribute:SOC-AC||Smeasure:0.832; wFmeasure:0.767; MAE:0.066; adpEm:0.872; meanEm:0.885; maxEm:0.895; adpFm:0.782; meanFm:0.793; maxFm:0.814
Method:ICON,Dataset:SOC,Attribute:SOC-BO||Smeasure:0.75; wFmeasure:0.841; MAE:0.166; adpEm:0.664; meanEm:0.784; maxEm:0.838; adpFm:0.833; meanFm:0.892; maxFm:0.914
Method:ICON,Dataset:SOC,Attribute:SOC-CL||Smeasure:0.792; wFmeasure:0.733; MAE:0.113; adpEm:0.821; meanEm:0.828; maxEm:0.833; adpFm:0.762; meanFm:0.767; maxFm:0.777
Method:ICON,Dataset:SOC,Attribute:SOC-HO||Smeasure:0.826; wFmeasure:0.763; MAE:0.091; adpEm:0.851; meanEm:0.854; maxEm:0.866; adpFm:0.788; meanFm:0.792; maxFm:0.815
Method:ICON,Dataset:SOC,Attribute:SOC-MB||Smeasure:0.783; wFmeasure:0.697; MAE:0.095; adpEm:0.813; meanEm:0.821; maxEm:0.834; adpFm:0.729; meanFm:0.738; maxFm:0.76
Method:ICON,Dataset:SOC,Attribute:SOC-OC||Smeasure:0.784; wFmeasure:0.704; MAE:0.103; adpEm:0.816; meanEm:0.821; maxEm:0.836; adpFm:0.739; meanFm:0.743; maxFm:0.765
Method:ICON,Dataset:SOC,Attribute:SOC-OV||Smeasure:0.784; wFmeasure:0.75; MAE:0.117; adpEm:0.824; meanEm:0.833; maxEm:0.84; adpFm:0.789; meanFm:0.792; maxFm:0.806
Method:ICON,Dataset:SOC,Attribute:SOC-SC||Smeasure:0.81; wFmeasure:0.721; MAE:0.079; adpEm:0.852; meanEm:0.856; maxEm:0.873; adpFm:0.728; meanFm:0.746; maxFm:0.782
Method:ICON,Dataset:SOC,Attribute:SOC-SO||Smeasure:0.769; wFmeasure:0.643; MAE:0.087; adpEm:0.803; meanEm:0.809; maxEm:0.828; adpFm:0.662; meanFm:0.677; maxFm:0.71

```

Tranined on DUTS, evaluated on SOC-Test(1200 pics)，又名S0C-1200。
```
Method:ICON,Dataset:SOC,Attribute:SOC-1200||Smeasure:0.811; wFmeasure:0.347; MAE:0.128; adpEm:0.812; meanEm:0.828; maxEm:0.896; adpFm:0.359; meanFm:0.363; maxFm:0.378
```

Trained on SOC-Sal-Train_and_Val(2400 pics), evaluated on SOC-Attr(9 attributes, 600 pics).
```
Method:ICON,Dataset:SOC,Attribute:SOC-AC||Smeasure:0.84; wFmeasure:0.778; MAE:0.062; adpEm:0.89; meanEm:0.885; maxEm:0.894; adpFm:0.803; meanFm:0.806; maxFm:0.822
Method:ICON,Dataset:SOC,Attribute:SOC-BO||Smeasure:0.7; wFmeasure:0.762; MAE:0.216; adpEm:0.599; meanEm:0.725; maxEm:0.787; adpFm:0.739; meanFm:0.811; maxFm:0.862
Method:ICON,Dataset:SOC,Attribute:SOC-CL||Smeasure:0.845; wFmeasure:0.803; MAE:0.08; adpEm:0.874; meanEm:0.883; maxEm:0.893; adpFm:0.835; meanFm:0.834; maxFm:0.847
Method:ICON,Dataset:SOC,Attribute:SOC-HO||Smeasure:0.841; wFmeasure:0.785; MAE:0.078; adpEm:0.873; meanEm:0.88; maxEm:0.892; adpFm:0.81; meanFm:0.815; maxFm:0.834
Method:ICON,Dataset:SOC,Attribute:SOC-MB||Smeasure:0.82; wFmeasure:0.746; MAE:0.072; adpEm:0.846; meanEm:0.862; maxEm:0.87; adpFm:0.772; meanFm:0.781; maxFm:0.794
Method:ICON,Dataset:SOC,Attribute:SOC-OC||Smeasure:0.813; wFmeasure:0.742; MAE:0.086; adpEm:0.847; meanEm:0.859; maxEm:0.873; adpFm:0.775; meanFm:0.78; maxFm:0.8
Method:ICON,Dataset:SOC,Attribute:SOC-OV||Smeasure:0.826; wFmeasure:0.801; MAE:0.089; adpEm:0.86; meanEm:0.872; maxEm:0.88; adpFm:0.833; meanFm:0.833; maxFm:0.844
Method:ICON,Dataset:SOC,Attribute:SOC-SC||Smeasure:0.834; wFmeasure:0.753; MAE:0.059; adpEm:0.895; meanEm:0.893; maxEm:0.906; adpFm:0.773; meanFm:0.779; maxFm:0.8
Method:ICON,Dataset:SOC,Attribute:SOC-SO||Smeasure:0.816; wFmeasure:0.714; MAE:0.061; adpEm:0.869; meanEm:0.873; maxEm:0.884; adpFm:0.734; meanFm:0.745; maxFm:0.766
```

Trained on SOC-Sal-Train(1800 pics), evaluated on SOC-Attr(9 attributes, 600 pics).
```
Method:ICON,Dataset:SOC,Attribute:SOC-AC||Smeasure:0.834; wFmeasure:0.774; MAE:0.067; adpEm:0.868; meanEm:0.891; maxEm:0.905; adpFm:0.781; meanFm:0.807; maxFm:0.827
Method:ICON,Dataset:SOC,Attribute:SOC-BO||Smeasure:0.718; wFmeasure:0.78; MAE:0.203; adpEm:0.421; meanEm:0.746; maxEm:0.781; adpFm:0.58; meanFm:0.825; maxFm:0.847
Method:ICON,Dataset:SOC,Attribute:SOC-CL||Smeasure:0.828; wFmeasure:0.774; MAE:0.092; adpEm:0.822; meanEm:0.868; maxEm:0.879; adpFm:0.778; meanFm:0.809; maxFm:0.827
Method:ICON,Dataset:SOC,Attribute:SOC-HO||Smeasure:0.834; wFmeasure:0.769; MAE:0.085; adpEm:0.857; meanEm:0.868; maxEm:0.882; adpFm:0.793; meanFm:0.802; maxFm:0.822
Method:ICON,Dataset:SOC,Attribute:SOC-MB||Smeasure:0.815; wFmeasure:0.746; MAE:0.079; adpEm:0.813; meanEm:0.853; maxEm:0.865; adpFm:0.754; meanFm:0.784; maxFm:0.808
Method:ICON,Dataset:SOC,Attribute:SOC-OC||Smeasure:0.786; wFmeasure:0.7; MAE:0.097; adpEm:0.816; meanEm:0.84; maxEm:0.856; adpFm:0.73; meanFm:0.743; maxFm:0.765
Method:ICON,Dataset:SOC,Attribute:SOC-OV||Smeasure:0.807; wFmeasure:0.769; MAE:0.103; adpEm:0.802; meanEm:0.851; maxEm:0.862; adpFm:0.779; meanFm:0.808; maxFm:0.822
Method:ICON,Dataset:SOC,Attribute:SOC-SC||Smeasure:0.819; wFmeasure:0.73; MAE:0.068; adpEm:0.867; meanEm:0.884; maxEm:0.903; adpFm:0.736; meanFm:0.759; maxFm:0.797
Method:ICON,Dataset:SOC,Attribute:SOC-SO||Smeasure:0.796; wFmeasure:0.675; MAE:0.071; adpEm:0.829; meanEm:0.848; maxEm:0.869; adpFm:0.69; meanFm:0.712; maxFm:0.745
```



## 4. 其他模型
另外20种模型在SOC上的预测图可在 [百度网盘|提取码: z3fq](https://pan.baidu.com/s/1eGGokt33eaZGsJ5n5VRt4Q)下载: [DSS](https://openaccess.thecvf.com/content_cvpr_2017/papers/Hou_Deeply_Supervised_Salient_CVPR_2017_paper.pdf)、[NLDF](https://openaccess.thecvf.com/content_cvpr_2017/papers/Luo_Non-Local_Deep_Features_CVPR_2017_paper.pdf)、[SRM](https://openaccess.thecvf.com/content_ICCV_2017/papers/Wang_A_Stagewise_Refinement_ICCV_2017_paper.pdf)、[Amulet](https://openaccess.thecvf.com/content_ICCV_2017/papers/Zhang_Amulet_Aggregating_Multi-Level_ICCV_2017_paper.pdf)、[DGRL](https://openaccess.thecvf.com/content_cvpr_2018/papers/Wang_Detect_Globally_Refine_CVPR_2018_paper.pdf)、[BMPM](https://openaccess.thecvf.com/content_cvpr_2018/papers_backup/Zhang_A_Bi-Directional_Message_CVPR_2018_paper.pdf)、[PiCANet-R](https://openaccess.thecvf.com/content_cvpr_2018/papers/Liu_PiCANet_Learning_Pixel-Wise_CVPR_2018_paper.pdf)、[R3Net](https://www.ijcai.org/Proceedings/2018/0095.pdf)、[C2S-Net](https://openaccess.thecvf.com/content_ECCV_2018/papers/Xin_Li_Contour_Knowledge_Transfer_ECCV_2018_paper.pdf)、[RANet](https://openaccess.thecvf.com/content_ECCV_2018/papers/Shuhan_Chen_Reverse_Attention_for_ECCV_2018_paper.pdf)、[CPD](https://openaccess.thecvf.com/content_CVPR_2019/papers/Wu_Cascaded_Partial_Decoder_for_Fast_and_Accurate_Salient_Object_Detection_CVPR_2019_paper.pdf)、[AFN](https://openaccess.thecvf.com/content_CVPR_2019/papers/Feng_Attentive_Feedback_Network_for_Boundary-Aware_Salient_Object_Detection_CVPR_2019_paper.pdf)、[BASNet](https://openaccess.thecvf.com/content_CVPR_2019/papers/Qin_BASNet_Boundary-Aware_Salient_Object_Detection_CVPR_2019_paper.pdf)、[PoolNet](https://openaccess.thecvf.com/content_CVPR_2019/papers/Liu_A_Simple_Pooling-Based_Design_for_Real-Time_Salient_Object_Detection_CVPR_2019_paper.pdf)、[SCRN](https://openaccess.thecvf.com/content_ICCV_2019/papers/Wu_Stacked_Cross_Refinement_Network_for_Edge-Aware_Salient_Object_Detection_ICCV_2019_paper.pdf)、[SIBA](https://openaccess.thecvf.com/content_ICCV_2019/papers/Su_Selectivity_or_Invariance_Boundary-Aware_Salient_Object_Detection_ICCV_2019_paper.pdf)、[EGNet](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhao_EGNet_Edge_Guidance_Network_for_Salient_Object_Detection_ICCV_2019_paper.pdf)、[F3Net](https://aaai.org/ojs/index.php/AAAI/article/view/6916)、[GCPANet](https://aaai.org/ojs/index.php/AAAI/article/view/6633)、[MINet](https://openaccess.thecvf.com/content_CVPR_2020/papers/Pang_Multi-Scale_Interactive_Network_for_Salient_Object_Detection_CVPR_2020_paper.pdf)。





如果你需要重新评估这些模型，或者其他的模型，可通过将`Attributes`文件夹放入预测文件夹，如`./maps/Prediction/MINet/SOC/Attributes`，然后稍微修改`Prediction/MINet/SOC/attr_categoty_and_generate_list.py`里的路径，即可自动划分9个属性。

另外，也可以测试SOC-Test，我们命名为原始的SOC-Test Set为 SOC-1200， 以下为另一个模型[SCWSSOD](https://arxiv.org/abs/2012.04404)的SOC-1200预测图，在[百度网盘|提取码: 0erf](https://pan.baidu.com/s/1PT_o31LTeXUJEYgXhDzNFg )可下载。
```
Method:SCWSSOD,Dataset:SOC,Attribute:SOC-1200||Smeasure:0.811; wFmeasure:0.332; MAE:0.115; adpEm:0.818; meanEm:0.842; maxEm:0.85; adpFm:0.352; meanFm:0.352; maxFm:0.355
```

比较表格(公平起见，我们也展示了用训练在DUTS上的参数生成的SOC预测显著图的效果):

![comp](comparison.png) 

## 5. 致谢
一些代码参考自:
* <https://github.com/lartpang/PySODMetrics> 

其它模型的SOC预测图来自:
* <https://github.com/wuzhe71/SCRN> 

## 引用

```text
@inproceedings{fan2018salient,
  title={Salient objects in clutter: Bringing salient object detection to the foreground},
  author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Jiang-Jiang and Gao, Shang-Hua and Hou, Qibin and Borji, Ali},
  booktitle={Proceedings of the European conference on computer vision (ECCV)},
  pages={186--202},
  year={2018}
}

@inproceedings{Smeasure,
    title={Structure-measure: A new way to evaluate foreground maps},
    author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
    booktitle=ICCV,
    pages={4548--4557},
    year={2017}
}

@inproceedings{Emeasure,
    title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
    author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
    booktitle=IJCAI,
    pages="698--704",
    year={2018}
}

@article{zhuge2021salient,
  title={Salient Object Detection via Integrity Learning},
  author={Zhuge, Mingchen and Fan, Deng-Ping and Liu, Nian and Zhang, Dingwen and Xu, Dong and Shao, Ling},
  journal={arXiv preprint arXiv:2101.07663},
  year={2021}
}
```

