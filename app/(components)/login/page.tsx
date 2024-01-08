import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
    Tabs,
    TabsContent,
    TabsList,
    TabsTrigger,
} from "@/components/ui/tabs"

const login = () => {
    return (
        <div className='container h-screen mx-auto'>
            <Tabs defaultValue="login" className="w-[400px]">
                <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="login">Login</TabsTrigger>
                    <TabsTrigger value="signup">Sign Up</TabsTrigger>
                </TabsList>

                <TabsContent value="login">
                    <Card>
                        <CardHeader>
                            <CardTitle>Log in to NeurJAM</CardTitle>
                            {/* <CardDescription>
                            Change your password here. After saving, you'll be logged out.
                        </CardDescription> */}
                        </CardHeader>
                        <CardContent className="space-y-2">
                            <div className="space-y-1">
                                <Label htmlFor="current">Email</Label>
                                <Input id="current" type="email" />
                            </div>
                            <div className="space-y-1">
                                <Label htmlFor="new">Password</Label>
                                <Input id="new" type="password" />
                            </div>
                        </CardContent>
                        <CardFooter>
                            <Button>Login</Button>
                        </CardFooter>
                    </Card>
                </TabsContent>

                <TabsContent value="signup">
                    <Card>
                        <CardHeader>
                            <CardTitle>Create an account on NeurJAM</CardTitle>
                            {/* <CardDescription>
                            Make changes to your account here. Click save when you're done.
                        </CardDescription> */}
                        </CardHeader>
                        <CardContent className="space-y-2">
                            <div className="space-y-1">
                                <Label htmlFor="name">First Name</Label>
                                <Input id="name" placeholder="Pedro" />
                            </div>
                            <div className="space-y-1">
                                <Label htmlFor="name">Last Name</Label>
                                <Input id="name" placeholder="Duarte" />
                            </div>
                            <div className="space-y-1">
                                <Label htmlFor="username">Username</Label>
                                <Input id="username" placeholder="@peduarte" />
                            </div>
                            <div className="space-y-1">
                                <Label htmlFor="email">Email</Label>
                                <Input id="username" placeholder="peduarte@test.com" />
                            </div>
                            <div className="space-y-1">
                                <Label htmlFor="password">Password</Label>
                                <Input id="password" type="password" />
                            </div>
                            <div className="space-y-1">
                                <Label htmlFor="confirmPassword">Confirm Password</Label>
                                <Input id="confirmPassword" type="password" />
                            </div>
                        </CardContent>
                        <CardFooter>
                            <Button>Sign Up</Button>
                        </CardFooter>
                    </Card>
                </TabsContent>
            </Tabs>

        </div>
    )
}


export default login