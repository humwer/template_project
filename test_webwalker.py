from locators import TestSite


def test_guest_surfed_on_site(walker):
    walker.go_to_url()
    assert walker.get_current_url() == TestSite.URL, "[-] Its not main page"
    print("[+] Success. We surfed to main page.")
