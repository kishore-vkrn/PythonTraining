import jenkins.model.Jenkins
import jenkins.model.*
import hudson.model.User
import hudson.security.*

// Read property from file
Properties properties = new Properties()
File propertiesFile = new File("/root/.jenkins/init.groovy.d/test.properties")
propertiesFile.withInputStream {
  properties.load(it)
}

// Pass Arguments to Variables
Admin_user = properties.'admin_user'
println "$Admin_user"
Admin_pass = properties.'admin_pass'
println "$Admin_pass"

// Create User
String[] arg = ["$Admin_user", "$Admin_pass", 'N'] as String[]
def instance = Jenkins.getInstance()
def hudsonRealm = new HudsonPrivateSecurityRealm(false)
def allUsers = User.getAll()
for (u in allUsers) {
  if (u.getId()== arg[0] ) {
    "${arg[0]} all ready exists in Jenkins"
  }else {
    hudsonRealm.createAccount(arg[0], arg[1])
    if (arg[2] =="Y"){
      def strategy = new GlobalMatrixAuthorizationStrategy()
      strategy.add(Jenkins.ADMINISTER, arg[0])
      instance.setAuthorizationStrategy(strategy)
    }
    else {
      println "$Admin_user" + " " + "$Admin_pass" + " " + "created"
    }
    instance.setSecurityRealm(hudsonRealm)
    instance.save()
  }
}

