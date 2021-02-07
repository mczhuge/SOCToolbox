# Efficient SOC Toolbox / [SOC快速评测工具(中文Readme)](https://github.com/mczhuge/SOCToolbox/edit/main/README_CN.md)

## 1. Datasets and Training Setting

Noted that, some early methods have used different training settings, this may cause unfair comparisons. So, the author of SOC recommend to use these setting:

- (1) using both train and val set to train your model. 
- (2) besides, it is better to drop images without salient objects for training and testing.

We have updated the Train(2400)/Test(1200+8 attributes) setting following above suggestions. 

For a quick employment, you can download the updated SOC on [Baidu | 提取码: iqul ](https://pan.baidu.com/s/1kWebPUhCQOCsvvAouo7eGQ). 

**If you download SOC on above link, you can ignore procedures below.**

----

(A) You can generates train.txt list which drops images without salient objects by


```
python ./datataset/SOC/Train/drop_blank_and_generate_list.py 
```

(B) You can segment 8 attribute of testing set and their test.txt by

```
python ./datasets/SOC/Test/attr_categoty_and_generate_list.py 
```

Then 8 file folders will be generated, which are `./datasets/SOC/Test/SOC-AC`, `./datasets/SOC/Test/SOC-BO`, `./datasets/SOC/Test/SOC-CL`, `./datasets/SOC/Test/SOC-HO`, `./datasets/SOC/Test/SOC-MB`, `./datasets/SOC/Test/SOC-OC`, `./datasets/SOC/Test/SOC-OV`, `./datasets/SOC/Test/SOC-SO`. They contain the images and GTs of each category.

**Actually, we have already processed A and B if you download SOC from above link.** (If needing, the original SOC dataset can be found [here](https://dpfan.net/socbenchmark/) and you can do A and B yourself.)

## 2. Evaluation

When your training process has done, you should generate the predictions of `SOC-AC`, `SOC-BO`, `SOC-CL`, `SOC-HO`, `SOC-MB`, `SOC-OC`, `SOC-OV` and `SOC-SO`, respectively.

An alternative method is to generate all SOC-Test, then modify the `attr_categoty_and_generate_list.py` to automatively split your predicted saliency maps.

After this, 

```
sh run_eval.sh
```

## 3. Results

## 4. Others methods 

## 5. Acknowledgement
Some codes are borrowed from:
* <https://github.com/lartpang/PySODMetrics> 

## Reference

```text
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
```

