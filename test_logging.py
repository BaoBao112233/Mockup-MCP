#!/usr/bin/env python3
"""
Quick test script for MCP Oxii-server tool logging
"""
import requests
import json

def test_mcp_endpoints():
    """Test the MCP server logging endpoints"""
    base_url = "http://localhost:9031"
    
    print("🧪 Testing MCP Oxii-server Tool Logging...")
    
    try:
        # Test health endpoint
        print("\n1. Health Check:")
        response = requests.get(f"{base_url}/health", timeout=5)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        
        # Test stats endpoint
        print("\n2. Tool Statistics:")
        response = requests.get(f"{base_url}/stats", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            stats = response.json()
            print(f"   Total Calls: {stats.get('total_calls', 0)}")
            print(f"   Available Tools: {list(stats.get('tool_calls', {}).keys())}")
        
        # Test logs endpoint
        print("\n3. Recent Logs:")
        response = requests.get(f"{base_url}/logs", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            logs = response.json()
            print(f"   Log Count: {len(logs.get('logs', []))}")
            recent = logs.get('logs', [])[-3:]
            for i, log in enumerate(recent, 1):
                print(f"   {i}. {log}")
        
        # Test docs.json endpoint
        print("\n4. Tool Documentation:")
        response = requests.get(f"{base_url}/docs.json", timeout=5)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            docs = response.json()
            print(f"   Server: {docs.get('name')}")
            print(f"   Tool Count: {docs.get('tool_count')}")
            tools = [tool['name'] for tool in docs.get('tools', [])]
            print(f"   Tools: {tools}")
        
        print("\n✅ All endpoints accessible!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to MCP server. Is it running on port 9031?")
        print("   Start with: python main.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_mcp_endpoints()
    
    print("\n📋 Available Endpoints:")
    print("• Health: http://localhost:9031/health")
    print("• Stats: http://localhost:9031/stats") 
    print("• Logs: http://localhost:9031/logs")
    print("• Docs: http://localhost:9031/docx")
    print("• Reset: curl -X POST http://localhost:9031/stats/reset")