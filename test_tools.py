#!/usr/bin/env python3
"""
Test script for OXII Smart Home MCP Server
"""
import asyncio
import sys
import os

# Add the tools directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))

from tools.auth import get_oxii_token
from tools.device_control import get_device_list

async def test_oxii_tools():
    """Test OXII tools functionality"""
    print("Testing OXII Smart Home Tools...")
    
    # Test credentials (you need to update these)
    test_phone = "0396056392"
    test_password = "abc123"
    test_country = "VI"
    
    try:
        # Test authentication
        print("\n1. Testing authentication...")
        token = await get_oxii_token(test_phone, test_password, test_country)
        
        if token and not token.startswith("Authentication"):
            print(f"✅ Authentication successful!")
            print(f"Token preview: {token[:20]}...")
            
            # Test getting device list
            print("\n2. Testing device list retrieval...")
            device_list = await get_device_list(token)
            
            if device_list and not device_list.startswith("Error"):
                print("✅ Device list retrieved successfully!")
                print("Device list preview:")
                print(device_list[:500] + "..." if len(device_list) > 500 else device_list)
            else:
                print(f"❌ Failed to get device list: {device_list}")
                
        else:
            print(f"❌ Authentication failed: {token}")
            
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("OXII Smart Home MCP Server Test")
    print("=" * 40)
    asyncio.run(test_oxii_tools())