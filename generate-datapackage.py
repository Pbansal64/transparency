# This file generates a datapackage.json file from the data located in the
# /data directory

from frictionless import describe
import os

package = describe("data/**/*.csv")
package.to_json("datapackage.json")
