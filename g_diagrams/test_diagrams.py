from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.programming.language import Java
from diagrams.programming.language import Typescript
from diagrams.programming.framework import Vue
from diagrams.programming.framework import Spring
from diagrams.programming.framework import Django
from diagrams.onprem.database import Mongodb, MongoDB,Mysql,Neo4J,Oracle



with Diagram("Web Service", show=False):
     Django("framework") >> Mongodb("database")