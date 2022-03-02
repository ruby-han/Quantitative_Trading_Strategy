{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0a219834",
   "metadata": {},
   "source": [
    "# Quantitative Trading Strategy\n",
    "#### By: Ruby Han\n",
    "\n",
    "## Abstract\n",
    "Forecasting market movement is a long-time attractive topic. This project aims to evaluate different algorithmic strategies on Apple, Microsoft, ExxonMobil, Chevron, Tesla using S&P 500 index as the benchmark over a one-year period (2021). An agent framework was built to trigger buy or sell orders with an initial capital of $10,000 based on selected strategy. Return on investment (ROI) was used as the performance metric. Base model outperformed other strategies with ROI of 31.5\\% but deep reinforcement learning model Evolution Strategy coming close in second place with ROI of 27.1\\%. Success of each strategy varied wildly with each stock for the time period. Machine learning models fared better than technical indicator models.\n",
    "\n",
    "## Problem Objective \n",
    "- Create a quantitative trading strategy for any stocks\n",
    "- No restriction on number of times entering or exiting the market, or long/short for period of strategy\n",
    "- Benchmark with S&P 500 index\n",
    "- Elucidate results and conclusion\n",
    "- Provide future work and considerations given more time and resources\n",
    "\n",
    "## Models Built\n",
    "\n",
    "**Base Model:**\n",
    "\n",
    "- Buy and Hold: Invest initial capital on first day and hold until last trading day\n",
    "\n",
    "**Technical Indicators:**\n",
    "\n",
    "- Bollinger Bands: Momentum model using moving standard deviations as bands\n",
    "\n",
    "- MACD: Moving average convergence divergence index\n",
    "\n",
    "**Machine Learning Models**\n",
    "\n",
    "- Evolution Strategy: Deep reinforcement learning model\n",
    "\n",
    "- LSTM: Long short-term memory model\n",
    "\n",
    "\n",
    "## Result Summary\n",
    "\n",
    "**Performance Metrix:**\n",
    "\n",
    "$$\\text{Return on Investment (ROI)}=\\frac{\\text{Current Value of Investment}-\\text{Investment Cost}}{\\text{Investment Cost}}$$\n",
    "\n",
    "![result_table](result_table.png)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
