---
# ============================================================
# RESUME CONFIGURATION — edit these to control all output
# ============================================================

meta:
  name: Justin R Meyer
  website_display: JustinRMeyer.com
  website_url: https://justinrmeyer.com
  linkedin_display: /in/justinrmeyercom
  linkedin_url: https://linkedin.com/in/justinrmeyercom
  phone: "303-834-7418"
  email: resume@justinrmeyer.com
  location: Denver, CO
  pdf_filename: justin-meyer-resume.pdf
  last_updated: "March 2026"

# ---- PDF Page Layout ----------------------------------------
pdf:
  page_size: letter          # letter | A4
  font_family: "Arial, sans-serif"
  font_size_body: "8.3pt"
  font_size_h1: "16pt"
  font_size_h2: "10pt"
  font_size_h3: "9pt"
  margin_top: "0.38in"
  margin_bottom: "0.38in"
  margin_left: "0.48in"
  margin_right: "0.48in"
  line_height: "1.3"
  color_accent: "#0066cc"
  color_text: "#000000"

# ---- Web Page Layout ----------------------------------------
web:
  font_family: "Arial, sans-serif"
  max_width: "820px"
  color_accent: "#0055aa"
  color_header_bg: "#f8f8f8"

# ---- SEO / Meta Tags ----------------------------------------
seo:
  page_title: "Justin Meyer — Technical Lead Manager & Site Reliability Engineer | Denver, CO"
  description: >
    26-year software and infrastructure engineering leader. Technical Lead Manager at AppOmni.
    Expert in SRE, DevOps, Kubernetes, cloud platforms (AWS/GCP/Azure), FedRAMP, and SOC2.
    MSc Data Engineering, PMP, CSM.
  keywords:
    - Site Reliability Engineer
    - Technical Lead Manager
    - SRE
    - DevOps
    - Platform Engineering
    - Kubernetes
    - Cloud Infrastructure
    - AWS
    - GCP
    - Azure
    - FedRAMP
    - SOC2
    - Python
    - Go
    - Golang
    - Terraform
    - Infrastructure as Code
    - AppOmni
    - Denver
    - Colorado
    - Staff Engineer
    - Engineering Manager
    - Data Engineering
    - FinOps
    - CUDA
    - NCCL
    - DCGM
    - PyTorch
    - SLURM
    - InfiniBand
    - Ceph
    - AI Infrastructure
    - GPU Infrastructure
    - HPC
  og_image: ""          # optional: full URL to a social preview image

# ---- Analytics ----------------------------------------------
analytics:
  google_tag: G-6P27RV7ZJJ
---

# Justin R Meyer

## Summary

Seasoned engineering leader with 26+ years spanning cloud infrastructure, site reliability, and AI/GPU systems. Proven record of building SRE organizations from scratch, driving FedRAMP/SOC2 compliance, and scaling multi-cloud platforms across regulated and high-throughput environments. Currently leading AI infrastructure and observability at Andromeda Cluster, focused on GPU-centric cloud platforms and distributed ML training pipeline reliability.

## Experience

### Andromeda Cluster — AI Infrastructure Engineer
**Dec 2025 – Present** | Denver, CO (Remote)

- Delivered escalated support for Andromeda customers, partnering directly with GPU hardware vendors to diagnose and resolve infrastructure-level hardware and storage issues across cloud environments.
- Launched the first aggregated observability platform for a heterogeneous fleet of Slurm clusters and raw GPU Kubernetes deployments, improving visibility, incident response time, and operational consistency.
- Managed AI/ML training pipeline infrastructure leveraging modern tools on distributed GPU clusters; integrated DCGM and NVIDIA NGC for GPU health monitoring and model deployment.
- Led regular Argo CD and Helm upgrade cycles, conducting peer reviews and enforcing deployment best practices to maintain platform stability and release reliability.

### AppOmni — Technical Lead Manager
**Jan 2025 – Dec 2025** | Denver, CO

- Served as DRI for FinOps operations and billing contract negotiations, ensuring financial efficiency and favorable vendor terms.
- Championed agile process improvements that elevated team discipline, visibility, and delivery predictability.
- Established a blameless incident culture and regular retrospectives, fostering continuous improvement and accountability while implementing FireHydrant to enhance incident response.

### AppOmni — Lead Site Reliability Engineer
**Nov 2023 – Jan 2025** | Denver, CO

- Grew SRE team from 1 to 5 engineers, improving operational resilience and efficiency.
- Managed and scaled SSPM/SEIM systems, supporting organizational security and compliance.
- Maintained FedRAMP and SOC2 compliance, bolstering stakeholder trust.
- Optimized cloud architecture, alleviating oversubscribed stacks and reducing costs.

### Crusoe — Staff Site Reliability Engineer
**Aug 2021 – Nov 2023** | Denver, CO (Remote)

- Ground-to-cloud management of GPU cloud offering.
- First SRE hire; grew and led the team to 6 members, scaling from 1 mobile data center to 5.
- Full lifecycle cloud infrastructure: PXE, MaaS, Ansible, Rocky Linux, libvirt, Tailscale, nginx/Pomerium, Kubernetes, gRPC.

### Adobe — Staff Site Reliability Engineer
**Jan 2021 – Aug 2021**

- GCP migration and alignment; led SDLC across multiple projects.
- AWS re-architect for Sales Connect.

#### Sr. Site Reliability Engineer — Marketo (Adobe)
**Mar 2019 – Jan 2021**

- Ongoing migration to containerized and cloud-native deployments.
- Monitoring and logging improvements for Marketo's bare-metal Kubernetes clusters.
- Management of 6k hosts via Puppet, pdsh, and Ansible.
- Unified authentication with sssd, pam.d, and corporate LDAP.

### eBay — Site Reliability Engineer
**Jul 2017 – Mar 2019** | Remote

- Covered 300B events/day across 6k services in the NOC/SEC.
- Expanded mobile market into China; implemented oAuth flows (Scala/Play, Python/Flask).
- Infrastructure as Code: Terraform, GCP, Drone CI/CD, chatbot integration.
- Multi-region monitoring, GKE cost analysis, log aggregation, HashiCorp Vault secrets management, fraud detection.

### AppThis — Full Stack Dev / SRE
**Jan 2017 – Jul 2017**

- AWS engineer: cost reduction, near 1B events/day throughput.
- Automation with Salt Stack.
- Custom HAProxy scaling with request processing SLA < 100ms.
- Log shipping migration to streams.
- PHP (HipHop, PHP7), Java, Scala (Play).

### CenturyLink — Full Stack Java Developer
**Nov 2016 – Jan 2017** | Contract

- VeuxDu team member on e911 and SpeakEasy projects.
- Java 1.8 + Spring Boot microservice migration.

### Starz Entertainment — Sr. Cloud Engineer
**Jun 2016 – Nov 2016**

- Maintained AWS and local tooling: Terraform, Consul, Nomad, Packer, Docker, Bamboo, Ansible.
- Built PaaS-agnostic redirect dashboard for starz.com (Meteor/Node + Angular2 frontend managing nginx cluster).

### Think Tank — Senior Developer
**2015 – Jun 2016**

- Full-stack Java developer supporting and maintaining hosted and installed SaaS collaboration product.
- Employed in-memory database for contribution-based transaction shipping and long polling.
- Led microservices migration from monolithic architecture.
- Stack: Spring Security, SAML2, Angular, Redis, ActiveMQ, DataDog.

### Rocket Science Innovation, LLC — Founder / Contract Developer
**2006 – 2019** | Remote / On-site

- Founder of a technology development company specializing in industrial IoT and infrastructure automation.
- 13-year engagement with Open Range Access: oilfield telemetry, edge data processing, and ETL to production ERP systems.
- Full-stack development across Python, JavaScript, and Java; hardware design including PCB layout, microcontroller firmware, and multi-modal comms (satellite, RF, cellular).
- Cloud architecture, VPC design, and on-premise to cloud migrations.

### Xilinx — System Developer
**2009 – 2015**

### Codeffects.com, LLC — Co-Founder
**2001 – 2006**

### University of Colorado Web Communications — Lead Developer
**1999 – 2006**

## Technical Skills

| Category | Technologies |
|---|---|
| **OS / Container** | Linux/Unix (Rocky, Debian), Kubernetes, Docker, Swarm, Podman |
| **Cloud Providers** | Crusoe, GCP, AWS, Azure, Digital Ocean |
| **AI / ML** | CUDA, NCCL, DCGM, PyTorch, SLURM, NVIDIA NGC, AI/ML pipelines, InfiniBand |
| **Storage / HPC** | Ceph, Weka, LightBits |
| **Testing** | Cypress, Headless Chrome, Selenium, Gatling, JMeter, QUnit, TDD |
| **Build Tools** | GitLab CI, Drone, Jenkins, SBT, Ant, Maven, Gradle, Nexus/Artifactory |
| **Source Control** | Git, SVN — ChatOps: hubot, yetibot, atlantis |
| **Programming** | Python, Perl, Java, JavaScript, Go, C/C++/C#, Scala, .NET/MVC, PHP, Ruby, embedded-VB, CSS, bash/zsh |
| **Deployment** | Argo, FluxCD, AWX, Helm, MaaS, Docker, Install4J, Ansible, Salt, Puppet, Packer, Terraform, Terragrunt |
| **Frameworks / Servers** | FastAPI, Flask, Django, Play, Spring, Sencha, jQuery, D3.js, Highcharts, Hibernate, MyBatis, CQ5 / Nginx, Apache, Caddy, Jetty, Tomcat, Node, Comet, IIS |
| **Databases** | PostgreSQL, MySQL, MongoDB, Cassandra, Elasticsearch, BigQuery, BigTable, Spanner, Redshift, RDS, PL/SQL, MSSQL, Flyway |
| **ETL / BI** | R-Project, Talend, Spark, POSIX RegEx |
| **Other** | Tailscale, HashiCorp Vault, PagerDuty, IAM, Hadoop, QEMU, VirtualBox, VMware, Parallels |

## Education

### University of Colorado at Boulder
**Aug 1999 – May 2004** — Bachelor of Computer Science

### General Assembly
**Oct – Dec 2019** — Data Science in Python

### Regis University Denver
**Aug 2020 – Mar 2023** — Master of Data Engineering, 4.0 GPA

## Professional Development

- Project Management Professional Certification (PMI.org)
- Coursera: Computing for Data Analysis; Data Analysis and Statistical Inference; Programming Mobile Applications for Android
- Udemy: Leadership Masterclass; 80/20 Product Ownership
- Certified Scrum Master (ScrumAlliance.org)

<!-- 
## Volunteer

- **AHS Advisory Board of Engineering and Computer Science**
-->
