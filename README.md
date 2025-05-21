# DRL for Real: Disentangled Representation Learning for Controllable Generation

## ICCV 2025 Workshop and Competition

### Workshop Overview

Disentangled representation learning (DRL) is believed to be one of the possible ways for AI to fundamentally understand the world, which potentially helps alleviate wicked problems like hallucination issues in Large Multimodal Models (LMMs/MLLMs) and controllability issues in Generative Models, ultimately contributing to progress toward Artificial General Intelligence (AGI). Over the years, disentangled representation learning has garnered significant academic interest and research contributions, recognized for its ability to improve model robustness, interpretability, and controllable generation capabilities.

However, the field currently faces a notable gap: the lack of comprehensive, realistic benchmarks and unified evaluation metrics that reflect real-world characteristics. This limitation has kept DRL confined mostly to synthetic toy scenarios, making it difficult to apply to more practical controllable generation applications where it could have significant impact.

### Competition Overview

To further promote the practical utility and real-world applicability of Disentangled Representation Learning, we are organizing this competition as part of the DRL for Real ICCV 2025 Workshop. The primary goal is to promote the development and evaluation of DRL methods on realistic datasets, thereby accelerating the transition of disentangled models from theoretical research to practical applications.

## Competition Tracks

The competition is divided into two main tracks:

### 1. Single-Factor Track

This track focuses on disentangled representation learning for single-factor variations in images. The dataset includes over 10,000 images covering multiple scenes, dozens of objects, and hundreds of factors of variation.

- **Dataset:** High-quality images with controlled single-factor variations
- **Requirement:** Participants must use disentangled models in this track
- **Evaluation:**
  - *Image Generation Quality (50%):* Measured using FID (Fréchet Inception Distance)
  - *Disentanglement Quality (50%):* Evaluated using Bi-directional DCI, which extends the traditional DCI metric by also measuring how perturbations in real images affect the corresponding latent variables in the encoder

### 2. Multi-Factor Track

This track is further divided into two sub-tracks, each with two leaderboards:

#### 2.1 General Image Dataset

- **Main Leaderboard:** Open to all methods (not restricted to disentangled approaches)
- **Disentanglement Leaderboard:** Only for disentangled methods
- **Evaluation for Main Leaderboard:** Uses LLM+VQA evaluation approach:
  - VQA assessment of whether models correctly generate images with attributes specified in given text
  - LLM evaluation of attribute strength in generated images
  - Comparison between text-specified attribute changes and LLM-detected attribute changes, with scores closer to 1 indicating better performance (minimal unintended attribute changes)
- **Evaluation for Disentanglement Leaderboard:** Same metrics as the Single-Factor Track (FID and Bi-directional DCI)

#### 2.2 Autonomous Driving Dataset

- **Main Leaderboard:** Open to all methods
- **Disentanglement Leaderboard:** Only for disentangled methods
- **Evaluation:** Similar to the General Image Dataset track, with domain-specific metrics

## Important Dates

- **Competition Announcement and Dataset Release:** May 25, 2025
- **Competition Submission Deadline:** June 25, 2025
- **Paper Submission Deadline:** June 30, 2025
- **Notification of Competition Results:** July 1, 2025
- **Notification of Paper Acceptance:** July 10, 2025
- **Final Documents Submission to ICCV:** August 15, 2025
- **Workshop and Competition Results Presentation:** October 2025 (during ICCV 2025)


## Paper Submissions

In addition to the competition, we welcome paper submissions related to disentangled representation learning, particularly those addressing:

- Novel disentanglement methods for real-world data
- Applications of disentangled representations in controllable generation
- Evaluation metrics for disentanglement quality
- Theoretical advances in understanding disentanglement

**Submission Deadline:** July 15, 2025

## Organizers

- Xin Jin, Professor, Eastern Institute of Technology, Ningbo, China
- Qiuyu Chen, Ph.D., Shanghai Jiao Tong University, Shanghai, China
- Yue Song, Professor, California Institute of Technology (Caltech), USA
- Xihui Liu, Professor, The University of Hong Kong, Hong Kong, China
- Shuai Yang, Professor, Peking University, Beijing, China
- Tao Yang, Dr., Xi'an Jiaotong University, Xi'an, China
- Ziqiang Li, Ph.D., Shanghai Jiao Tong University, Shanghai, China
- Jianguo Huang, Ph.D., Eastern Institute of Technology, Ningbo, China
- Yuntao Wei, Ph.D., The Hong Kong Polytechnic University, Hong Kong, China
- Ba'ao Xie, Professor, Eastern Institute of Technology, Ningbo, China
- Nicu Sebe, Professor, Fellow of IAPR, University of Trento, Italy
- Wenjun (Kevin) Zeng, Professor, IEEE Fellow, Eastern Institute of Technology, Ningbo, China

## Assistance

- Zhenyu Hu, Engineer, Institute of Digital Twin, EIT, Ningbo, China

## Contact

For any questions regarding the workshop or competition, please contact:
- Xin Jin (jinxin@eitech.edu.cn), Professor, Eastern Institute of Technology, Ningbo, China
- Qiuyu Chen (canghaimeng@sjtu.edu.cn), Ph.D., Shanghai Jiao Tong University, Shanghai, China

---

*This workshop and competition are organized in collaboration with leading research institutions and industry partners committed to advancing the field of disentangled representation learning.*
