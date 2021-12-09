import unittest
from AFW.Alerts import AlertTests
from AFW.BrowserWindows import BrowserWindowTests
from AFW.Frames import FramesTests
from AFW.Modals import ModalTests
from AFW.NestedFrames import NestedFrameTests

from Elements.Links import LinksTests
from Elements.Images import ImagesTests
from Elements.Buttons import ButtonTests
from Elements.RadioButton import RadioButtonTests
from Elements.TextBox import TextBoxTests
from Elements.CheckBox import CheckBoxTests
from Elements.DynamicProperties import DynamicPropertiesTests
from Elements.UploadDownload import UploadDownloadTests
from Elements.webTables import WebTableTests

from Forms.Forms import FormTests

from Interactions.Droppable import DropabbleTests
from Interactions.Draggable import DraggableTests
from Interactions.Sortable import SortableTests
from Interactions.Selectable import SelectTests
from Interactions.Resizable import ResizableTests

from Widgets.Menu import MenuTests
from Widgets.Tabs import TabTests
from Widgets.Sliders import SliderTests
from Widgets.ToolTips import ToolTipTests
from Widgets.DatePicker import DatePickerTests
from Widgets.Accordian import AccordionTests
from Widgets.Autocomplete import AutoCompleteTests
from Widgets.ProgressBar import ProgressBarTests

# loading test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(AlertTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(BrowserWindowTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(FramesTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ModalTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(NestedFrameTests)

tc6 = unittest.TestLoader().loadTestsFromTestCase(LinksTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(ImagesTests)
tc8 = unittest.TestLoader().loadTestsFromTestCase(ButtonTests)
tc9 = unittest.TestLoader().loadTestsFromTestCase(RadioButtonTests)
tc10 = unittest.TestLoader().loadTestsFromTestCase(TextBoxTests)
tc11 = unittest.TestLoader().loadTestsFromTestCase(CheckBoxTests)
tc12 = unittest.TestLoader().loadTestsFromTestCase(DynamicPropertiesTests)
tc13 = unittest.TestLoader().loadTestsFromTestCase(UploadDownloadTests)
tc14 = unittest.TestLoader().loadTestsFromTestCase(WebTableTests)

tc15 = unittest.TestLoader().loadTestsFromTestCase(FormTests)

tc16 = unittest.TestLoader().loadTestsFromTestCase(DraggableTests)
tc17 = unittest.TestLoader().loadTestsFromTestCase(DropabbleTests)
tc18 = unittest.TestLoader().loadTestsFromTestCase(SelectTests)
tc19 = unittest.TestLoader().loadTestsFromTestCase(SortableTests)
tc20 = unittest.TestLoader().loadTestsFromTestCase(ResizableTests)

tc21 = unittest.TestLoader().loadTestsFromTestCase(MenuTests)
tc22 = unittest.TestLoader().loadTestsFromTestCase(TabTests)
tc23 = unittest.TestLoader().loadTestsFromTestCase(ToolTipTests)
tc24 = unittest.TestLoader().loadTestsFromTestCase(SliderTests)
tc25 = unittest.TestLoader().loadTestsFromTestCase(ProgressBarTests)
tc26 = unittest.TestLoader().loadTestsFromTestCase(DatePickerTests)
tc27 = unittest.TestLoader().loadTestsFromTestCase(AccordionTests)
tc28 = unittest.TestLoader().loadTestsFromTestCase(AutoCompleteTests)

# creating test Suite

FuncTestSuite = unittest.TestSuite(
    [tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, tc11, tc12, tc13, tc14, tc15, tc16, tc17, tc18, tc19, tc20,
     tc21, tc22, tc23, tc24, tc25, tc26, tc27, tc28])

# running the Test Suite
unittest.TextTestRunner().run(FuncTestSuite)
