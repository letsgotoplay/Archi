# Database Seeder for InnerSource Hub PoC
# Populates the database with initial sample data.

from sqlalchemy.orm import Session
from . import models

def seed_db(db: Session):
    # Check if data exists
    if db.query(models.User).first():
        return

    print("Seeding database...")

    # Create Users
    users = [
        models.User(email="alice@company.com", department="Engineering", skills="Java, Kafka", avatar_url="https://i.pravatar.cc/150?u=alice"),
        models.User(email="bob@company.com", department="Data Science", skills="Python, PyTorch", avatar_url="https://i.pravatar.cc/150?u=bob"),
        models.User(email="charlie@company.com", department="Frontend", skills="React, CSS", avatar_url="https://i.pravatar.cc/150?u=charlie"),
    ]
    db.add_all(users)
    db.commit()

    # Re-query users to get IDs
    alice = db.query(models.User).filter_by(email="alice@company.com").first()
    bob = db.query(models.User).filter_by(email="bob@company.com").first()
    charlie = db.query(models.User).filter_by(email="charlie@company.com").first()

    # Create Projects
    projects = [
        models.Project(
            name="Centralized Logging Wrapper",
            description="A unified wrapper for Log4j and SLF4J to enforce structured logging across all Java services.",
            problem_statement="Every team writes their own logging config, leading to inconsistent logs in Splunk.",
            status=models.ProjectStatus.IDEA,
            owner_id=alice.id,
            tags="Java, Logging, Splunk",
            help_wanted_roles="QA"
        ),
        models.Project(
            name="Kafka Monitoring Tool",
            description="Dashboard to visualize consumer lag and topic throughput in real-time.",
            problem_statement="No visibility into consumer lag for critical pipelines.",
            status=models.ProjectStatus.POC,
            vcs_url="https://github.com/company/kafka-monitor",
            owner_id=alice.id,
            tags="Go, Kafka, React",
            help_wanted_roles="Frontend"
        ),
        models.Project(
            name="React UI Kit",
            description="Standardized UI components following the company design system.",
            problem_statement="Inconsistent UI across internal tools.",
            status=models.ProjectStatus.BUILD,
            vcs_url="https://github.com/company/ui-kit",
            owner_id=charlie.id,
            tags="React, CSS, Storybook",
            help_wanted_roles="Designer"
        ),
        models.Project(
            name="Data Pipeline Orchestrator",
            description="Airflow plugins for standard data ingestion patterns.",
            problem_statement="Duplicated code in every DAG.",
            status=models.ProjectStatus.SCALE,
            vcs_url="https://github.com/company/airflow-plugins",
            owner_id=bob.id,
            tags="Python, Airflow",
        ),
        models.Project(
            name="Internal API Gateway",
            description="A lightweight gateway for internal microservices authentication.",
            problem_statement="Security is handled differently in every service.",
            status=models.ProjectStatus.IDEA,
            owner_id=bob.id,
            tags="Rust, Security"
        ),
         models.Project(
            name="Feature Flag Service",
            description="Simple API to manage feature toggles.",
            problem_statement="Hardcoded feature flags require deployments to change.",
            status=models.ProjectStatus.IDEA,
            owner_id=alice.id,
            tags="Python, Redis"
        ),
         models.Project(
            name="Customer 360 View",
            description="Aggregated view of customer data from 5 different sources.",
            problem_statement="Support agents have to open 5 tabs to help a customer.",
            status=models.ProjectStatus.POC,
            vcs_url="https://github.com/company/c360",
            owner_id=charlie.id,
            tags="Node.js, GraphQL"
        ),
         models.Project(
            name="Automated Compliance Checker",
            description="CI/CD step to verify regulatory compliance.",
            problem_statement="Compliance audits are manual and slow.",
            status=models.ProjectStatus.IDEA,
            owner_id=bob.id,
            tags="Bash, Docker"
        ),
         models.Project(
            name="Mobile App Analytics",
            description="Custom analytics SDK for our mobile apps.",
            problem_statement="Third party tools are too expensive.",
            status=models.ProjectStatus.BUILD,
            vcs_url="https://github.com/company/mobile-analytics",
            owner_id=alice.id,
            tags="Swift, Kotlin"
        ),
         models.Project(
            name="DevOps Dashboard",
            description="One place to see build status, deployments, and alerts.",
            problem_statement="Too many tools to check for system health.",
            status=models.ProjectStatus.IDEA,
            owner_id=charlie.id,
            tags="Vue, Grafana"
        )
    ]
    db.add_all(projects)
    db.commit()

    print("Database seeded successfully.")
