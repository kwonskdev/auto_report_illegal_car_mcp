#!/usr/bin/env python3
"""
MCP Server for Safety Report Tools using FastMCP
Provides tools for traffic violation reporting and get address from geocoding
"""

import logging
from typing import Dict, Any

from fastmcp import FastMCP
from report import run_report, reverse_geocoding

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("safety-report-tools")


@mcp.tool(
    name="report_traffic_violation",
    description="Report traffic violation",
)
def report_traffic_violation(
    title: str,
    description: str,
    vehicle_number: str="12허3456",
    violation_type: str="02",
    latitude: float=33.5072,    
    longitude: float=126.4938,
    video_files: list[str] = None,
    reporter_name: str = "익명",
    reporter_phone: str = "비공개",
    reporter_email: str = "비공개"
) -> str:

    return run_report(
        title=title, 
        vehicle_number=vehicle_number, 
        violation_type=violation_type, 
        latitude=latitude, 
        longitude=longitude, 
        description=description, 
        video_files=video_files, 
        reporter_name=reporter_name, 
        reporter_phone=reporter_phone, 
        reporter_email=reporter_email
        )


@mcp.tool(
    name="get_address_from_geocoding",
    description="Reverse geocoding to get address from latitude and longitude",
)
def get_address_from_geocoding(
    latitude: float=33.5072,
    longitude: float=126.4938
) -> str:
    result = reverse_geocoding(latitude, longitude)
    return result

if __name__ == "__main__":
    mcp.run()