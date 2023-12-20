# coding: utf-8
#
import uiautomator2 as u2
import time

d = u2.connect()

d(description="Open menu").click()
d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/nav_list"]/android.widget.RelativeLayout[9]').click()
d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/recyclerView"]/android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
d(description="Open menu").click()
d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/nav_list"]/android.widget.RelativeLayout[2]').click()
d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/fragmentLayout"]/android.widget.LinearLayout[1]').click()
d(resourceId="de.danoeh.antennapod.debug:id/sbPosition").click()
d.click(0.929, 0.79)
d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/audioplayerFragment"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/android.widget.ImageButton[1]').click()
time.sleep(60)