# Explaining predictions using Neural Additive Models (NAMs)
Re-Implemetation of Paper - https://arxiv.org/pdf/2004.13912.pdf

* Team members: Sai Pradeep Peri, Kinori Rosnow
* Project paper: https://github.com/class-data-mining-master/2021-spring-fml-project-team01-test/blob/main/Final%20Report.pdf
* Project Presentation: https://github.com/class-data-mining-master/2021-spring-fml-project-team01-test/blob/main/Final%20Presentation%20Slides.pdf

## Description
As powerful function approximators, Deep Neural Networks are widely used in many real-world applications. But due to their complex structure, they are considered Black-box models which cannot be explained or interpreted on how they make predictions. While many existing methods use surrogate models to explain and interpret DNN predictions, few methods exist to explain predictions at a global view. As a result linear and other simpler models are employed due to their higher transparency, but often with a reduction in performance.

In an attempt to combine the best attributes of linear models and DNNs we explore Neural Additive models (NAMs). NAMs are a sub-family of General Additive Models suggested by Agarwal et. al. which leverage much of the performance of DNNs while maintaining inherent interpretability Agarwal et. al. NAM’s learn linear combinations of networks, each attending to a single feature. Interpreting NAMs is easy as the impact of a feature on the prediction does not rely on the other features and can be understood by visualizing its corresponding shape function (e.g., plotting fi(xi) vs. xi). These graphs learned by NAMs are not just an explanation but an exact description of how NAMs compute a prediction. This could help harness the expressivity of neural nets on high-stakes domains with intelligibility requirements. 

## Prerequisites
The required dependencies are included in the requirements.txt
```
pip install -r requirements.txt
```

## Authors
Sai Pradeep Peri sap187@pitt.edu <br>
Kinori Rosnow ksr43@pitt.edu

## Acknowledgments
Thanks to the paper Authors and google for open sourcing the code https://github.com/google-research/google-research/tree/master/neural_additive_models

### Inspiration
Repositories referenced and learned from:
* https://github.com/AmrMKayid/nam
* https://github.com/kherud/neural-additive-models-pt
* https://github.com/nickfrosst/neural_additive_models

## License

```
@misc{kayid2020nams,
  title={Neural additive models Library},
  author={Kayid, Amr and Frosst, Nicholas and Hinton, Geoffrey E},
  year={2020}
}
```

```
@article{agarwal2020neural,
  title={Neural additive models: Interpretable machine learning with neural nets},
  author={Agarwal, Rishabh and Frosst, Nicholas and Zhang, Xuezhou and Caruana, Rich and Hinton, Geoffrey E},
  journal={arXiv preprint arXiv:2004.13912},
  year={2020}
}
```
```
@article{nori2019interpretml,
  title={InterpretML: A Unified Framework for Machine Learning Interpretability},
  author={Nori, Harsha and Jenkins, Samuel and Koch, Paul and Caruana, Rich},
  journal={arXiv preprint arXiv:1909.09223},
  year={2019}
}
```
