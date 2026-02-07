"""
Skills Database Module
Maintains a comprehensive list of technical skills for matching
"""

# Programming Languages
PROGRAMMING_LANGUAGES = [
    'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'c', 'go', 'rust',
    'ruby', 'php', 'swift', 'kotlin', 'scala', 'r', 'matlab', 'perl', 'shell',
    'bash', 'powershell', 'sql', 'html', 'css', 'dart', 'lua', 'haskell', 'erlang',
    'elixir', 'clojure', 'f#', 'vb.net', 'objective-c', 'assembly', 'fortran',
    'cobol', 'pascal', 'ada', 'delphi'
]

# Web Frameworks
WEB_FRAMEWORKS = [
    'flask', 'django', 'fastapi', 'express', 'react', 'angular', 'vue', 'next.js',
    'nuxt.js', 'svelte', 'ember', 'backbone', 'meteor', 'spring', 'spring boot',
    'asp.net', 'laravel', 'symfony', 'codeigniter', 'ruby on rails', 'phoenix',
    'gin', 'echo', 'fiber', 'play framework', 'akka', 'vert.x', 'ktor'
]

# Frontend Technologies
FRONTEND_TECH = [
    'html5', 'css3', 'sass', 'scss', 'less', 'bootstrap', 'tailwind css',
    'material-ui', 'ant design', 'chakra ui', 'styled-components', 'jquery',
    'redux', 'mobx', 'zustand', 'recoil', 'webpack', 'vite', 'parcel', 'rollup',
    'gulp', 'grunt', 'npm', 'yarn', 'pnpm', 'babel', 'typescript', 'es6', 'es7'
]

# Backend Technologies
BACKEND_TECH = [
    'node.js', 'deno', 'bun', 'rest api', 'graphql', 'grpc', 'microservices',
    'serverless', 'lambda', 'azure functions', 'google cloud functions',
    'web sockets', 'socket.io', 'rabbitmq', 'kafka', 'redis', 'celery',
    'rq', 'bull', 'sidekiq', 'background jobs', 'cron', 'scheduled tasks'
]

# Databases
DATABASES = [
    'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 'cassandra',
    'oracle', 'sql server', 'sqlite', 'dynamodb', 'neo4j', 'couchdb',
    'influxdb', 'timescaledb', 'cockroachdb', 'mariadb', 'firebase',
    'firestore', 'supabase', 'planetscale', 'prisma', 'sequelize', 'typeorm'
]

# Cloud Platforms
CLOUD_PLATFORMS = [
    'aws', 'azure', 'google cloud', 'gcp', 'heroku', 'digitalocean', 'linode',
    'vultr', 'cloudflare', 'vercel', 'netlify', 'render', 'fly.io', 'railway',
    'aws ec2', 'aws s3', 'aws lambda', 'aws rds', 'aws dynamodb', 'aws ecs',
    'aws eks', 'azure app service', 'azure functions', 'azure cosmos db',
    'gcp compute engine', 'gcp cloud functions', 'gcp cloud sql', 'kubernetes',
    'docker', 'docker compose', 'terraform', 'ansible', 'jenkins', 'gitlab ci',
    'github actions', 'circleci', 'travis ci', 'azure devops'
]

# DevOps & Tools
DEVOPS_TOOLS = [
    'git', 'github', 'gitlab', 'bitbucket', 'svn', 'mercurial', 'jenkins',
    'gitlab ci', 'github actions', 'circleci', 'travis ci', 'azure devops',
    'jira', 'confluence', 'trello', 'asana', 'notion', 'slack', 'microsoft teams',
    'docker', 'kubernetes', 'helm', 'istio', 'linkerd', 'prometheus', 'grafana',
    'elk stack', 'splunk', 'datadog', 'new relic', 'sentry', 'logstash', 'kibana'
]

# Data Science & ML
DATA_SCIENCE_ML = [
    'machine learning', 'deep learning', 'neural networks', 'tensorflow', 'pytorch',
    'keras', 'scikit-learn', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'plotly',
    'jupyter', 'colab', 'spark', 'hadoop', 'hive', 'pig', 'airflow', 'prefect',
    'mlflow', 'kubeflow', 'opencv', 'nltk', 'spacy', 'transformers', 'bert',
    'gpt', 'llm', 'langchain', 'openai', 'computer vision', 'nlp'
]

# Testing Frameworks
TESTING_FRAMEWORKS = [
    'pytest', 'unittest', 'nose', 'junit', 'testng', 'jest', 'mocha', 'chai',
    'cypress', 'selenium', 'playwright', 'puppeteer', 'karma', 'jasmine',
    'rspec', 'phpunit', 'xunit', 'nunit', 'gtest', 'cucumber', 'behave',
    'robot framework', 'postman', 'insomnia', 'rest assured', 'karate'
]

# Mobile Development
MOBILE_TECH = [
    'react native', 'flutter', 'ionic', 'xamarin', 'swift', 'kotlin', 'objective-c',
    'android studio', 'xcode', 'appium', 'expo', 'firebase', 'onesignal',
    'push notifications', 'in-app purchases', 'mobile ui', 'mobile ux'
]

# Other Technologies
OTHER_TECH = [
    'linux', 'unix', 'windows', 'macos', 'bash scripting', 'powershell',
    'api design', 'oauth', 'jwt', 'oauth2', 'openid connect', 'saml',
    'ldap', 'active directory', 'nginx', 'apache', 'iis', 'load balancing',
    'cdn', 'ssl', 'tls', 'https', 'dns', 'tcp/ip', 'http', 'rest', 'soap',
    'xml', 'json', 'yaml', 'toml', 'csv', 'excel', 'power bi', 'tableau',
    'looker', 'metabase', 'superset'
]


def get_all_skills():
    """
    Returns a comprehensive list of all skills
    Normalized to lowercase for matching
    """
    all_skills = (
        PROGRAMMING_LANGUAGES +
        WEB_FRAMEWORKS +
        FRONTEND_TECH +
        BACKEND_TECH +
        DATABASES +
        CLOUD_PLATFORMS +
        DEVOPS_TOOLS +
        DATA_SCIENCE_ML +
        TESTING_FRAMEWORKS +
        MOBILE_TECH +
        OTHER_TECH
    )
    
    # Remove duplicates and normalize
    unique_skills = list(set([skill.lower().strip() for skill in all_skills]))
    
    # Also add multi-word variations
    extended_skills = unique_skills.copy()
    
    # Add common variations
    variations = {
        'python': ['python3', 'python 3'],
        'javascript': ['js', 'ecmascript'],
        'typescript': ['ts'],
        'c++': ['cpp', 'c plus plus'],
        'c#': ['csharp', 'c sharp'],
        'html': ['html5'],
        'css': ['css3'],
        'react': ['reactjs', 'react.js'],
        'angular': ['angularjs', 'angular.js'],
        'vue': ['vuejs', 'vue.js'],
        'node.js': ['nodejs', 'node'],
        'aws': ['amazon web services'],
        'gcp': ['google cloud platform'],
        'ml': ['machine learning'],
        'ai': ['artificial intelligence'],
        'api': ['rest api', 'restful api'],
        'sql': ['structured query language'],
    }
    
    for key, values in variations.items():
        if key in extended_skills:
            extended_skills.extend(values)
    
    return list(set(extended_skills))


# Export the skills list
SKILLS_DATABASE = get_all_skills()

