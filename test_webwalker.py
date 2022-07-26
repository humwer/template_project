from locators import TestSite


def test_guest_surfed_on_site(walker):
    walker.go_to_url()
    assert walker.get_current_url() == TestSite.URL, "[-] Its not main page"
    print("[+] Success. We surfed to main page.")


def test_guest_can_go_to_catalog(walker):
    walker.go_to_url()
    walker.click_this_element(TestSite.BUTTON_GO_TO_CATALOG)
    assert walker.text_of_this_element(TestSite.IS_CATALOG) == 'Women', "[-] It's not 'Women-page'"
    print("[+] Success. We surfed to women-page from main page.")


class TestCatalog:

    def test_guest_can_click_category(self, walker):
        walker.go_to_url()
        walker.click_this_element(TestSite.BUTTON_GO_TO_CATALOG)
        walker.click_this_element(TestSite.CATEGORY_TOPS)
        assert walker.get_attribute_of_element(TestSite.CATEGORY_TOPS, 'checked') == 'true', \
            "[-] Checkbox 'Tops' isnt checked"
        print("[+] Checkbox 'Tops' is checked")

    def test_guest_not_clicked_category(self, walker):
        walker.go_to_url()
        walker.click_this_element(TestSite.BUTTON_GO_TO_CATALOG)
        assert walker.get_attribute_of_element(TestSite.CATEGORY_DRESSES, 'checked') is None, \
            "[-] Checkbox 'Dresses' is checked"
        print("[+] Checkbox 'Dresses' isnt checked")
