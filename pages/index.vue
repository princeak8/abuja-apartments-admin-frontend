<template>
  <div class="mx-auto h-screen">
    <div class="flex h-full">
      <div class="flex-1 h-full">
        <img src="/images/landing.jpg" width="100%" height="100%" alt="landing page image" class="object-cover h-full" />
      </div>
      <div class="flex-1 flex h-full items-center justify-center">
        <Card class="w-[450px]">
          <CardHeader>
            <CardTitle>Login</CardTitle>
          </CardHeader>
          <CardContent>
            <form>
              <div class="grid items-center w-full gap-4">
                <div class="flex flex-col space-y-1.5">
                  <Label for="name">Username</Label>
                  <Input id="name" placeholder="Type your username" />
                </div>
                <div class="flex flex-col space-y-1.5">
                  <Label for="password">Password</Label>
                  <Input id="password" placeholder="Type your password" />
                </div>
              </div>
            </form>
          </CardContent>
          <CardFooter class="flex justify-between px-6">
            <Button @click="handleSubmit">Login</Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  </div>
</template>

<script setup>
  function handleSubmit() {
    navigateTo("/dashboard");
  }
</script>
