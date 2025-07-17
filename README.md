# 🚁 Airfoil Noise Prediction with Apache Spark

A machine learning project that predicts airfoil noise levels using Apache Spark and PySpark. This project implements a complete ML pipeline to analyze the relationship between airfoil design parameters and sound pressure levels.

## 📊 Dataset

This project uses the **Airfoil Self-Noise Dataset** from the UCI ML Repository (ID: 291), which contains NASA data from various airfoil blade sections tested in an anechoic wind tunnel.

### Features:

- **Frequency** (Hz) - Sound frequency
- **Attack Angle** (degrees) - Angle of attack of the airfoil
- **Chord Length** (meters) - Distance from leading to trailing edge
- **Free-stream Velocity** (m/s) - Velocity of air flow
- **Suction Side Displacement Thickness** (meters) - Boundary layer thickness

### Target:

- **Sound Pressure Level** (decibels) - Scaled sound pressure level

## 🛠️ Technology Stack

- **Apache Spark 3.5.0** - Distributed computing framework
- **PySpark 4.0.0** - Python API for Spark
- **Python 3.12** - Programming language
- **Docker & Docker Compose** - Containerization
- **scikit-learn compatible pipeline** - ML workflow

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Python App    │────│  Spark Master   │────│  Spark Worker   │
│   (Development) │    │   (Cluster)     │    │   (Execution)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                      ┌─────────────────────┐
                      │   Docker Network    │
                      └─────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- VS Code with Dev Containers extension (recommended)

### Running the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/jans108/airfoil-project.git
   cd airfoil-project
   ```

2. **Start with Docker Compose**

   ```bash
   docker-compose up --build
   ```

3. **Or use VS Code Dev Containers**
   - Open in VS Code
   - Command Palette → "Dev Containers: Reopen in Container"

## 📈 Machine Learning Pipeline

The project implements a complete ML pipeline with the following stages:

1. **Data Ingestion** - Fetch data from UCI ML Repository
2. **Data Preprocessing** - Clean, deduplicate, and transform data
3. **Feature Engineering** - Vector assembly and standardization
4. **Model Training** - Linear regression with cross-validation
5. **Model Evaluation** - RMSE, R², and MAE metrics
6. **Model Persistence** - Save trained model for future use

### Pipeline Stages:

```python
VectorAssembler → StandardScaler → LinearRegression
```

## 📊 Model Performance

The trained model provides predictions for airfoil noise levels with evaluation metrics:

- **RMSE** (Root Mean Squared Error)
- **R²** (Coefficient of Determination)
- **MAE** (Mean Absolute Error)

## 🔧 Development

### Project Structure

```
airfoil-project/
├── Dockerfile                 # Python app container
├── docker-compose.yml         # Multi-service orchestration
├── requirements.txt           # Python dependencies
├── main.py                   # ML pipeline implementation
├── .devcontainer/            # VS Code dev container config
│   ├── devcontainer.json
│   └── docker-compose.yml
└── README.md                 # This file
```

### Services

- **airfoil-app**: Python development environment with Java 17
- **spark-master**: Spark cluster coordinator (port 8080 - Web UI)
- **spark-worker**: Spark task executor

### Accessing Spark Web UI

Visit [http://localhost:8080](http://localhost:8080) to monitor Spark jobs and cluster status.

## 🎯 Use Cases

- **Aerospace Engineering**: Optimize airfoil designs for noise reduction
- **Wind Energy**: Improve wind turbine blade acoustics
- **Aviation**: Research aircraft noise pollution

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NASA** for providing the airfoil self-noise dataset
- **UCI Machine Learning Repository** for hosting the dataset
- **Apache Spark** community for the distributed computing framework
- **Bitnami** for providing excellent Spark Docker images

⭐ If you found this project helpful, please give it a star!
