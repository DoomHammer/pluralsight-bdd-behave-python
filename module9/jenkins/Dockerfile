FROM jenkins/jenkins:lts
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt
USER root
RUN apt-get update \
&& apt-get install -y --no-install-recommends allure docker.io docker-compose python3 python3-pip python3-venv \
&& rm -rf /var/lib/apt/lists/*
COPY casc.yaml /var/jenkins_home/casc.yaml
